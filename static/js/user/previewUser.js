$(document).on("ready",init_page);

function init_page(){

    $("input#id_username").on({
        keydown: function(e) {
        if (e.which === 32)
            return false;
        },
        change: function() {
            this.value = this.value.replace(/\s/g, "");
        }
    });

    var file, 
    render;

    $("#upload_button").on("click", function(){
        $("#profile_input").click();
    });

    $("#profile_input").on("change", function(ev){
        file = ev.target.files[0];
        if(!file.type.match("image.*")) {
            alert("This file isn't image or it's unsupported format");
            return;
        }

        var fd = new FormData();
        fd.append("file", file);
        fd.append("csrfmiddlewaretoken",document.getElementsByName('csrfmiddlewaretoken')[0].value);

        $.ajax({
            type: "POST",
            url: "/crop-avatar/" ,  // or just url: "/my-url/path/"
            processData: false,
            contentType: false,
            data:fd,
            success: function(data) {
                $("figure img").attr("src",""+data+"");
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log("Ha Ocurrido el Siguiente Error:" +errorThrown+xhr.status+xhr.responseText);
            }
        });
    });
}