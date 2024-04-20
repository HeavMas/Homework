#!/bin/bash

# Проверяем, что скрипт запущен с правами суперпользователя
if [ $EUID -ne 0 ]
then
    echo "Please run this as root!"
    exit 1
fi
# Получаем имя пользователя, который инициировал сессию
VIRT_USER=`logname`

# Установка необходимых пакетов для работы с виртуализацией
apt install qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager ovmf

# Создаем переменную GRUB, содержащую текущие настройки GRUB
GRUB=`cat /etc/default/grub | grep "GRUB_CMDLINE_LINUX_DEFAULT" | rev | cut -c 2- | rev`

# Создаем резервную копию конфигурации GRUB для возможного восстановления
cat /etc/default/grub > grub_backup.txt
chmod +x uninstall.sh

# Определяем, используется ли процессор Intel
CPU=$(lscpu | grep GenuineIntel | rev | cut -d ' ' -f 1 | rev )

INTEL="0"

if [ "$CPU" = "GenuineIntel" ]
then
    INTEL="1"
fi

# Формируем строку для активации IOMMU в зависимости от типа процессора
if [ $INTEL = 1 ]
then
    IOMMU="intel_iommu=on kvm.ignore_msrs=1"
    echo "Set Intel IOMMU On"
else
    IOMMU="amd_iommu=on kvm.ignore_msrs=1"
    echo "Set AMD IOMMU On"
fi

# Формируем новую строку настроек GRUB
OLD_OPTIONS=`cat /etc/default/grub | grep GRUB_CMDLINE_LINUX_DEFAULT | cut -d '"' -f 1,2`
NEW_OPTIONS="$OLD_OPTIONS $IOMMU\""
echo $NEW_OPTIONS

# Обновляем GRUB
sed -i -e "s|^GRUB_CMDLINE_LINUX_DEFAULT.*|${NEW_OPTIONS}|" /etc/default/grub

# Предлагаем пользователю проверить и при необходимости отредактировать конфигурацию GRUB
echo 
echo "Grub was modified to look like this: "
echo `cat /etc/default/grub | grep "GRUB_CMDLINE_LINUX_DEFAULT"`
echo 
echo "Do you want to edit it? y/n"
read YN

if [ $YN = y ]
then
    nano /etc/default/grub
fi

# Применяем изменения в GRUB
update-grub

# Добавляем пользователя в группу libvirt
usermod -a -G libvirt $VIRT_USER

# Копируем скрипт переопределения для vfio
cp vfio-pci-override-vga.sh /etc/initramfs-tools/scripts/init-top/vfio-pci-override-vga.sh
chmod 744 /etc/initramfs-tools/scripts/init-top/vfio-pci-override-vga.sh

# Обновляем initramfs
if [ ${1-0} = "-e" ]
then
    update-initramfs -u
else
    update-initramfs -u 2> /dev/zero
fi

