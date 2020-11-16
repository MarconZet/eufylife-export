# EufyLife export
Export your body data collected by Eufy Smart Scale from app to CSV

## Requirements
* Linux (or WSL)
* Python 3.7+

## How it works
There is no way to export data using official means.
It's time to get creative.
By default, application stores body fat history locally.
That's why you don't require continuous internet to use it.
We can use that for our advantage.

## How to use
### 1. Acuire backup file
The first step is to get a backup file which contains the data we want
#### On Android
Download your backup from GoogleDrive put it inside the folder with the script
#### On IOS
The program was made with the android system in mind.
If you are an IOS user, you will have to do some additional work.
* Download AndroidStudio
* Create a new AVD with Play Store
* Download EufyLife application on your phone
* Log in, wait for the application to pull data from the server
* Run the following command: `adb backup -noapk com.oceanwing.smarthome`

And you will have your very own backup.ab file
### 2. Run the script
Once you have your ab file (I'm going to assume it's called backup.ab), put it inside the folder and run the following command
```shell script
./run.sh backup.ab
```
The result being body_stats.csv file, containing your body fat data
