mkdir -p ~/altair_software_recruitment/executables/
echo '#!/usr/bin/env python3' > ~/altair_software_recruitment/executables/hello_altair.py
echo 'print("Hello Altair!")' >> ~/altair_software_recruitment/executables/hello_altair.py
sudo chown root:root ~/altair_software_recruitment/executables/hello_altair.py
sudo chmod 700 ~/altair_software_recruitment/executables/hello_altair.py