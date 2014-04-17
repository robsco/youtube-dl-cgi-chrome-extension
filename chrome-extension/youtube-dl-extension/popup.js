// change me

var serverScript = "http://nirvana-vpn.intelcompute.com/cgi-bin/youtube-dl.cgi";

// pre-populate the form with the current url
chrome.tabs.getSelected(null,function(tab) {
    document.getElementById('url').value = tab.url;
});

// add onClick to form button
window.addEventListener('load', function(evt) {
    document.getElementById('button').addEventListener('click', submitDownload);
});

// get the current queue contents
$.getJSON(
    serverScript,
    function(data){
        parseQueue(data);
    }
);

// show the queue contents in popup.html
function parseQueue(data){
    urls = data.urls;

    pre = document.getElementById('status');

    if ( urls.length ){
        pre.innerHTML = "In the queue...\n\n";

        for (i=0; i< urls.length; i++){
            pre.innerHTML += urls[i] + "\n";
        }
    }
    else{
        pre.innerHTML = "Nothing in the queue.\n\n";
    }
}

// make call to download this url
function submitDownload() {
    document.getElementById('status').innerHTML = "Requesting...\n\n";

    $.getJSON(
        serverScript + "?url=" + encodeURIComponent(document.getElementById('url').value),
        function(data){
            parseQueue(data);
        }
    );
};
