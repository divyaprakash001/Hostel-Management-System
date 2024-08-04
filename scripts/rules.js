
$(document).ready(function () {

    
    // $('input[type="text"]').focus(function () {
    //     $(this).siblings('.l_move').css({ 'top': '0%' })
    // });
    $.ajax({
        method: 'post',
        url: 'pythonfile/user.py',
        data: {
            what: "fetchroomid",
            user:'Yes'
        },
        success: function (data) {
            console.log(data)
            if (data.includes('all detail fetched!!')){
                var data_val=data.split('&&');
                $('#us_brow').html(data_val[4].trim());
            }
            else{
                swal('Warning','Please Do One Entry In Room Details and User Details!!','warning')
            }
        }
    });
    $("#id").change(function () {
        // e.preventDefault();

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "checkuserid",
                userid: $("#id").val().trim()
            },
            success: function (data) {
                console.log(data)
                if (data.includes("Userid doesnot exist"))
                    swal({
                        title: "Failed!",
                        text: "Userid doesnot exit",
                        icon: "error",
                    });
            }
        });

    });
    $("#rules_submit").on("click", function (e) {
        e.preventDefault();


        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what:"rules_insertion",
                userid: $("#id").val().trim(),
                rules_area: $("#rules_area").val().trim(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("rules inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Rules Inserted Successfully!",
                        icon: "success",
                    }).then((value)=>{
                        location.reload();
                    })
                }
                else if(data.includes('already exists!!')){
                    swal({
                        title: "Warning!",
                        text: "Rules already exists for this userid!",
                        icon: "warning",
                    });
                }
                else if (data.includes("one of the field is empty")) {
                    swal({
                        title: "Failed!",
                        text: "One of the field is empty!",
                        icon: "error",
                    });
                } else {
                    swal({
                        title: "Failed!",
                        text: "Sorry for inconvenience!",
                        icon: "error",
                    });
                }
            }
        });


    });



});