function testMicroservice(data, url) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            tag = document.getElementById('output');

            if (tag == undefined){
                alert(xmlhttp.responseText);
            } else {
                tag.innerHTML = xmlhttp.responseText;
            }

        }
      };

    xmlhttp.open("POST", url);

    var data = JSON.stringify({string: data});

    xmlhttp.send(data);

}


function callMicroservice() {
    data = document.getElementById('data').value;
    url = document.getElementById('url').value;
    testMicroservice(data, url);


}