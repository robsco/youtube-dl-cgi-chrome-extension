youtube-dl-cgi-chrome-extension
===============================

Chrome extension and Perl CGI script to download videos to your own server

The Problem
===========

youtube-dl is a tool for downloading videos from many different sites, such as YouTube and BBC iPlayer.

Opening a terminal to run the script and copy the URL is a pain.

Installing dubious software/toolbars, etc. is worrying.

The Solution
============

A simple Chrome Extension that, when activated, sends the current URL to a CGI script hosted on your own server.

The CGI scripts forks and executes the youtube-dl script.

All your videos are downloaded to one central location.



HowTo
=====

Install youtube-dl...

http://rg3.github.io/youtube-dl/download.html

Put the youtube-dl.cgi script on a webserver that can execute Perl CGI scripts.

Modify the constant lines for the location of the youtube-dl script, and the folder to store downloaded videos.

Sub folders are created with the datestamp.

In Chrome, navigate to chrome://extensions, tick the checkbox for "Developer Mode", then click the "Load unpacked extension" button, and navigate to the chrome-extension folder in this checkout.
