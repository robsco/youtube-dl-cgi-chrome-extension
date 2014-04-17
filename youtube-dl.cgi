#!/bin/env perl

use strict;
use warnings;

use CGI;

# change me

use constant YOUTUBE_DL   => '/usr/local/bin/youtube-dl';
use constant DOWNLOAD_DIR => '/home/username/youtube-dl';
use constant PARENT_SLEEP => 1;

my $url = CGI->new->param('url');

respond() && exit if ! $url;

$url =~ s/"//g;

# fork, child starts downloading, parent shows the queue

if ( my $pid = fork )
{
    sleep PARENT_SLEEP;   # give the child time to start
    respond();
}
else
{
    my @urls = get_queue();

    exit if grep { $_ eq $url } @urls;   # already in the queue?

    close STDIN;
    close STDOUT;

    my $cmd = YOUTUBE_DL . ' "' . $url . '"';

    my ( $sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst ) = localtime( time );

    $year += 1900;
    $mon += 1;
    $mon =~ s/^(\d)$/0$1/;
    $mday =~ s/^(\d)$/0$1/;

    my $folder = join('-', $year, $mon, $mday);

    if ( ! -d DOWNLOAD_DIR . '/' . $folder )
    {
        mkdir DOWNLOAD_DIR . '/' . $folder;
    }

    chdir DOWNLOAD_DIR . '/' . $folder;

    `$cmd`;
}

sub respond
{
    my @urls = get_queue();
    print "Content-Type: application/json; charset=utf8\n\n";
    print as_json( @urls );  
}

sub get_queue
{
    my @output = `ps -ef | grep python | grep youtube-dl | grep -v grep`;

    my @urls = ();

    foreach my $output ( @output )
    {
        chomp($output);
        my @fields = split(' ', $output);
        push @urls, $fields[ -1 ];
    }

    return @urls;
}

sub as_json
{
    my @urls = @_;

    my $json = "{\"urls\":[";

    foreach my $url ( @urls )
    {
        $json .= "\"$url\"";
        $json .= "," if $url ne $urls[-1];
    }

    $json .= "]}";

    return $json;
}
