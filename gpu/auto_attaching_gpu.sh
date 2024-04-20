#!/bin/bash

# Путь к файлу, где хранится последнее состояние VM
STATE_FILE="/home/fillipov/vm-gpu_test/demo_tiger_state.txt"
# Путь к XML файлу конфигурации устройства
GPU_CONFIG="/home/fillipov/vm-gpu_test/gpu_passthrough.xml"

# Функция для проверки состояния VM и выполнения действий
function check_and_attach {
    current_state=$(virsh list --all | grep "demo_tiger" | awk '{print $3}')
    
    # Проверяем, существует ли файл состояния, если нет, создаем его с пустым значением
    if [ ! -f "$STATE_FILE" ]; then
        echo "" > $STATE_FILE
    fi

    last_state=$(cat $STATE_FILE)

    # Проверяем, изменилось ли состояние на running
    if [[ "$current_state" == "running" && "$last_state" != "running" ]]; then
        echo "VM 'demo_tiger' has just started. Attaching GPU..."
        virsh attach-device demo_tiger $GPU_CONFIG
    fi

    # Обновляем файл состояния
    echo $current_state > $STATE_FILE
}

# Запуск функции в бесконечном цикле с паузой 3 секунды
while true; do
    check_and_attach
    sleep 3
done
