youtube-dl-cgi-chrome-extension
===============================

Chrome extension and Perl CGI script to download videos to your own server

The Problem
-----------

youtube-dl is a tool for downloading videos from many different sites, such as YouTube and BBC iPlayer.

Opening a terminal to run the script and copy the URL is a pain.

Installing dubious software/toolbars, etc. to download videos from websites is worrying.

The Solution
------------

A simple Chrome Extension that, when activated, sends the current URL to a CGI script hosted on your own server.

The CGI scripts forks and executes the youtube-dl script.

All your videos are downloaded to one central location.


HowTo
-----

### youtube-dl

Install youtube-dl on your server...

http://rg3.github.io/youtube-dl/download.html

### CGI Script

Put the youtube-dl.cgi script on a webserver that can execute Perl CGI scripts.

On RH/CentOS this is in /var/www/cgi-bin/.

I can only speak for RedHat/CentOS servers with these commands to install the Apache webserer...

```
$ yum install httpd
$ chkconfig --level 345 on httpd on
```

Note: The aim for this project was to keep everything as simple as possible, the CGI script is nothing special, and has minimal dependencies, it only requires CGI.

For RedHat/CentOS, you may need...

```
$ yum install perl
$ yum install cpan
$ cpan CGI
```

Modify the constant lines for the location of the youtube-dl script, and the folder to store downloaded videos.

Make sure the user running the webserver has permission to write to the folder you create.

Sub-folders are created with the datestamp where the videos are actually downloaded to.

### Chrome Extension

Edit popup.js in the chrome-extension folder and modify the serverScript variable to point to your servers web address and specifically the CGI script.

In Chrome, navigate to chrome://extensions, tick the checkbox for "Developer Mode", then click the "Load unpacked extension" button, and navigate to the chrome-extension folder.

Icon should now appear in Chrome, Opening the extension makes a call to the script and will show if anything is currently downloading on the server.
