# Smartbytes-Tracker
Python Script To Track Remaining Data

Smartbytes is a service provided by Airtel ( Indian ISP ) to check one's remaining broadband data or
update their plans.

This script uses python's ('requests' and 'bs4') libraries to access the smartbytes page and fetch the
amount of data remaining.

**********************************************************************************************************
I created this script to remind me to go slow on data utilization at the end of the month because
once the plan is completely used up, the speed really sucks. So this script keeps reminding me every hour
to keep check on my data uses.

I run this script using crontab, which starts it as a service at the boot time.

Crontab command:
	crontab -e
		add the following line:
			@reboot path-to-the-file
**********************************************************************************************************