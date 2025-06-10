while ($true) {
    # Definir la dirección a monitorear
    $servidor = "google.com"

    # Ruta del archivo log
    $logPath = "C:\Scripts\Logs\log_red.txt"

    # Obtener la fecha y hora actual
    $fecha = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    # Hacer ping y guardar resultado
    if (Test-Connection -ComputerName $servidor -Count 1 -Quiet) {
        Add-Content -Path $logPath -Value "$fecha - Conexión exitosa a $servidor"
    } else {
        Add-Content -Path $logPath -Value "$fecha - Error de conexión a $servidor"
    }

    # Esperar 10 minutos antes de repetir
    Start-Sleep -Seconds 600
}
