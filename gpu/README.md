# GPU Attaching 
Один  из вариантов проброски видеокарты на варитуалку
 
## Включение IOMMU и привязка к VFIO
Если коротко, то для проброса требуется включить компонент аппаратного обеспечения IOMMU, который позволит работать устройствам непосредственно с физ. памятью минуя ОС. Затем требуется подвязать
нужную  видеокарту к драйверам VFIO( Virtual Function Input/Output, драйвера, которые в сочетании с IOMMU дают вм прямой доступ к ресурсам пк). Также важно не забыть подвязать и аудио-порт, который идет
в одной связке с видеокартой. Все это есть в скрипте gpu_passtrough, его достаточно выполнить и все выполнится автоматически 
## Проброс видеокарты 
Т.к на данный момент работа ведётся с qemy-kvm и libvirt для проброски нужен xml файл с данными видеокарты. gpu_passtorugh.xml 

## Автоматическая проброска 
В ходе теста было выявлено, что при перезапуске вм привязка видеокарты слетала и приходилось руками её заново ставить, поэтому был разработан скрипт, который будет автоматически пробрасывать видеокарту
каждый раз когда вм будет включаться. Скрипт надо сделать процессом демоном, чтобы он автоматически запускался каждый раз с запуском сервера
