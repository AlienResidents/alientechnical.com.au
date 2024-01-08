Title: Alien Technical
Date: 2010-12-03 10:20
Category: Blog

Stuff
```
#!/bin/bash

declare result retval server
declare -a servers

mapfile -t servers < <(grep -Ev '^#|^$'  "${HOME}"/git/github/alienresidents/dotfiles/tings.txt)

echo -e "Starting apt upgrades..."
for server in "${servers[@]}"
do
  echo -e "================================== Upgrading \"${server}\" =================================="
  ping -c 1 "${server}" &> /dev/null
  retval=$?
  if [[ ${retval} = 0 ]]; then
    result=$(ssh root@"${server}" "TERM=vt100 apt --allow-releaseinfo-change update && apt -o Dpkg::Options::=\"--force-confold\" -y --purge --autoremove upgrade" < /dev/null 2>&1)
    retval=$?
    if [[ ${retval} = 0 ]]; then
      echo -e "Upgrade successful (${server})"
    else
      echo -e "Updated Failed (${server}):"
      echo -e "${result}"
    fi
  fi
done
echo -e "Finished apt upgrades."
```

```
sensors
nouveau-pci-0200
Adapter: PCI adapter
fan1:         931 RPM
temp1:        +38.0°C  (high = +95.0°C, hyst =  +3.0°C)
                       (crit = +105.0°C, hyst =  +5.0°C)
                       (emerg = +135.0°C, hyst =  +5.0°C)

corsairpsu-hid-3-b
Adapter: HID adapter
v_in:        230.00 V  
v_out +12v:   12.06 V  (crit min =  +8.41 V, crit max = +15.59 V)
v_out +5v:     5.01 V  (crit min =  +3.50 V, crit max =  +6.50 V)
v_out +3.3v:   3.31 V  (crit min =  +2.31 V, crit max =  +4.30 V)
psu fan:        0 RPM
vrm temp:     +41.2°C  (crit = +70.0°C)
case temp:    +30.5°C  (crit = +70.0°C)
power total:  86.00 W  
power +12v:   68.00 W  
power +5v:    15.00 W  
power +3.3v:   4.00 W  
curr +12v:     5.25 A  (crit max = +85.00 A)
curr +5v:      3.06 A  (crit max = +40.00 A)
curr +3.3v:    1.25 A  (crit max = +40.00 A)

acpitz-acpi-0
Adapter: ACPI interface
temp1:        +27.8°C  (crit = +119.0°C)
temp2:        +29.8°C  (crit = +119.0°C)

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +37.0°C  (high = +84.0°C, crit = +100.0°C)
Core 0:        +34.0°C  (high = +84.0°C, crit = +100.0°C)
Core 1:        +37.0°C  (high = +84.0°C, crit = +100.0°C)
Core 2:        +37.0°C  (high = +84.0°C, crit = +100.0°C)
Core 3:        +35.0°C  (high = +84.0°C, crit = +100.0°C)
```

```
 linnie  /home/cdd/testing/pelican/content/images  kube.l.cdd.net.au  default    
 cdd   ls -l
total 68
-rw-rw-r-- 1 cdd cdd 67646 Jan  8 17:48 favicon.ico
 linnie  /home/cdd/testing/pelican/content/images  kube.l.cdd.net.au  default    
 cdd  
```
