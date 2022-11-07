call :LOG [INFO] Starting proxy daemon...

set PROXY=true

@rem Store original proxy settings
for /f "tokens=2*" %%a in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable 2^>nul') do set "ORIG_PROXY_ENABLE=%%b"
for /f "tokens=2*" %%a in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer 2^>nul') do set "ORIG_PROXY_SERVER=%%b"

@rem TODO: External proxy when ORIG_PROXY_ENABLE == 0x1
echo set ws = createobject("wscript.shell") > "%temp%\proxy.vbs"

@rem CA certificate for HTTPS scheme
call :LOG [INFO] Waiting for CA certificate generation...
set CA_CERT_FILE="%USERPROFILE%\.mitmproxy\mitmproxy-ca-cert.cer"

set /a TIMEOUT_COUNT=0

:CERT_CA_CHECK
if not exist %CA_CERT_FILE% (
	timeout /t 1 >nul 2>nul
	set /a TIMEOUT_COUNT+=1
	goto CERT_CA_CHECK
)
:EXTRA_TIMEOUT
if %TIMEOUT_COUNT% LEQ 2 (
	timeout /t 1 >nul 2>nul
	set /a TIMEOUT_COUNT+=1
	goto EXTRA_TIMEOUT
)
call :LOG [INFO] Adding CA certificate to store...
certutil -addstore root %CA_CERT_FILE% >nul 2>nul

call :LOG [INFO] Setting up network proxy...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f >nul 2>nul
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "127.0.0.1:8080" /f >nul 2>nul

:EXIT
if "%DATABASE%" == "" (
	call :LOG [INFO] MongoDB daemon not started, no need to clean up.
) else (
	call :LOG [INFO] Shutting down MongoDB daemon...
	taskkill /t /f /im mongod.exe >nul 2>nul
)
if "%PROXY%" == "" (
	call :LOG [INFO] Proxy daemon not started, no need to clean up.
) else (
	call :LOG [INFO] Restoring network settings...

	reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d "%ORIG_PROXY_ENABLE%" /f >nul 2>nul
	reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "%ORIG_PROXY_SERVER%" /f >nul 2>nul

	call :LOG [INFO] Shutting down proxy daemon...
	taskkill /t /f /im mitmdump.exe >nul 2>nul

	call :LOG [INFO] Removing CA certificate...
	for /F "tokens=2" %%s in ('certutil -dump %CA_CERT_FILE% ^| findstr ^"^sha1^"') do (
		set SERIAL=%%s
	)

	certutil -delstore root %SERIAL% >nul 2>nul
)

call :LOG [INFO] See you again :)
goto :EOF

:LOG
echo [%time:~0,8%] %*