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
