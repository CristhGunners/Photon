$(document).on("ready",init_page);

function init_page(){
    var file, 
    render;

    $("#upload_button").on("click", function(){
        $("#background_input").click();
    });

    document.body.addEventListener("drop", function(ev){
        file = ev.dataTransfer.files[0];
        if(!file.type.match("image.*")) {
            alert("This file isn't image or it's unsupported format");
            return;
        }
        reader = new FileReader();
        reader.addEventListener("load", (function(theFile) {
            return function(e) {
            $("figure.preview img").css({
                'display':'block',
            });
            $("figure.preview img").attr("src",""+e.target.result+"");
        };
    })(file), false);
        reader.readAsDataURL(file);
    }, false);

    $("#background_input").on("change", function(ev){
        file = ev.target.files[0];
        if(!file.type.match("image.*")) {
            alert("This file isn't image or it's unsupported format");
            return;
        }
        reader = new FileReader();
        reader.addEventListener("load", (function(theFile) {
            return function(e) {
                $("figure.preview img").css({
                    'display':'block',
                });
                $("figure.preview img").attr("src",""+e.target.result+"");
            };
        })(file), false);
        reader.readAsDataURL(file);
    });
}