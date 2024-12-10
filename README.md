# MinecraftServer-LogParsing
Python script(s) to parse logs from a Minecraft server for better analysis in a spreadsheet.

## Current Uses
Current script is just for parsing out server connects/disconnects and normalizing the data in a CSV (time, action, user) for further analysis in a spreadsheet.

## Prerequisites
NOTE: these instructions assume that the minecraft server is running in docker using the [container created by itzg](https://github.com/itzg/docker-minecraft-bedrock-server). It is likely that the logs are formatted the same for other Minecraft servers but the method for obtaining the logs may be different. It is also assumed that python3 is installed on the system being used to run the script. Tested on macOS Sequoia.

## Instructions
1. Copy repo to system (or atleast just the desired .py file).
2. To obtain logs to be parsed, run command `docker container logs [container-name] > minecraftlogs.txt` on the host where the server is running. Sudo may be required if the logged in user is not part of the docker group.
3. Copy the .txt file obtained above into the same directory as the .py script in step 1.
4. Execute the script by running `python3 parseconnections.py` while in the same directory as the downloaded script (may need to run `chmod +x parseconnections.py` first).

## Output
The output should be a file in the same directory named `serverconnections.csv` who's contents should look something like this: 
```
Time,Action,Username
2024-11-21 15:59:54,Connected,[username]
2024-11-21 16:00:13,Disconnected,[username]
2024-11-21 16:02:55,Connected,[username]
2024-11-21 16:15:56,Disconnected,[username]
2024-11-21 16:20:58,Connected,[username]
2024-11-21 16:29:59,Disconnected,[username]
```
