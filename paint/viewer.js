fetch('test.txt')
  .then(response => response.text())
  .then((data) => {
   //console.log(data)
    
    update(data.split("\n"))
  })




var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);



function createBinaryString (nMask) {
    // nMask must be between -2147483648 and 2147483647
    for (var nFlag = 0, nShifted = nMask, sMask = ""; nFlag < 32;
         nFlag++, sMask += String(nShifted >>> 31), nShifted <<= 1);
    return sMask;
  }

function update(data){

    ctx.fillStyle = "black";
    for(var x = 0; x < 8; x++){
        binary_string = createBinaryString(data[x])
        console.log(data[x])
        //console.log((pic[x] >>> 0).toString(2));
        binary_string = binary_string.slice(24,32)
        console.log(binary_string)
        for(var col = 0; col < 8; col++){
            if(binary_string[col] == 1){
            ctx.fillRect(col * 50, x*50, 50, 50);
            }

        }
    }

   //var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");  // here is the most important part because if you dont replace you will get a DOM 18 exception.


    //window.location.href=image; // it will save locally
    filename = data[8] + ".png"
    var link = document.getElementById('link');
    link.setAttribute('download', filename);
    link.innerHTML = "Download " + filename;
    link.setAttribute('href', canvas.toDataURL("image/png").replace("image/png", "image/octet-stream"));
    //link.click();
}

