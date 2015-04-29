ISU Web Portal
===
### Primary Contributors
* Andrew Guibert
* Andrew Hartman
* Jonathan Mielke
* Lucas Rorhet
* Travis Reed 

===
### Resources
* [Trello Board](https://trello.com/b/kPAKvBao/senior-design)
* [Group Website](http://may1518.ece.iastate.edu/)
* [Project Plan](https://drive.google.com/a/iastate.edu/file/d/0B6mbCLySBSQxOUxYQ196eUY5cXc/view?usp=sharing)

===
### Deplyoment Instructions
01. Package the source folder locally (except for the settingslocal)<br>
`zip -r build-MM-DD.zip ./src -x '*/settingslocal.py'`
02. Transfer archive to vrac server <br>
`scp ./build-MM-DD.zip username@nirwebportal.vrac.iastate.edu:/home/nirwebportal/archives/`
03. SSH into nirwebportal.vrac.iastate.edu <br>
`ssh <yourusername>@nirwebportal.vrac.iastate.edu`
04. Stop currently running server process(es) <br>
`ps -au<yourusername>` then `kill <pid>`\
05. Store the current settingslocal.py in a safe place.  Then remove old source and extract new build archive <br>
`unzip build-MM-DD.zip`
06. Replace the src folder with the new build
07. Move settingslocal.py from your safe place to the /src folder.
08. Reset database if schema changes were made since last build
09. Ensure database.db is writeable
10. Start the server <br>
`python src/run_sandbox.py 2> stderr.log &`
