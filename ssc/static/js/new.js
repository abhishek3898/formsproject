window.onload = function () { 

    const bikes = ["Honda", "Kawasaki", "Ninja"];
    const f = bikes.entries();
    for (let x of f) {
        var nodes = document.getElementsByClassName('constructor')
        // console.log(nodes)
        for(var i=0; i < nodes.length; i++){
            nodes[i].innerHTML += x + '<br>';
            console.log(nodes[i])
        };
        // console.log('x')
    
    }
  
}
 