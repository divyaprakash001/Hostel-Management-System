
$(document).ready(function () {

$("#search_user").on("click",function(e){
    e.preventDefault();
    window.location.href= "Userservice.html";
})

    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });

    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="user.html";
    })

    let imageDataUrl1 = "";


    // image data url for image 1
    $("#pic").on("change", function (event) {
        var file = event.target.files[0];
        var reader = new FileReader();

        reader.onload = function (event) {
            imageDataUrl1 = event.target.result;
            $('#pic').after(`<a href="${imageDataUrl1}" class="view-image" style="float:left;">Uploaded Image</a>`);
        };

        if (file) {
            reader.readAsDataURL(file);
        } else {
            console.error("No file selected.");
        }
    });



    $("#submit_btn").on("click", function (e) {
        e.preventDefault();

        // alert($("#id").val())
        // alert(imageDataUrl1)
        // alert($('input[name="gender"]:checked').val())

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "user_details_insertion",
                emp_id: $("#id").val().trim(),
                emp_name: $("#name").val().trim(),
                emp_contact: $("#contact").val().trim(),
                emp_gender: $('input[name="gender"]:checked').val(),
                emp_dob: $("#dob").val(),
                emp_blood: $("#bloodgrp").val(),
                emp_father: $("#f_name").val().trim(),
                emp_mother: $("#m_name").val().trim(),
                emp_par_contact: $("#p_contact").val().trim(),
                emp_photo: imageDataUrl1,
                emp_aadhar: $("#aadhar").val().trim(),
                emp_street: $("#street").val().trim(),
                emp_dist_state: $("#dit").val().trim(),
                emp_pincode: $("#pin").val().trim(),
                emp_local_guard: $("#local_guard").val().trim(),
                emp_local_guard_cont: $("#local_guard_contact").val().trim(),
                emp_local_guard_addr: $("#local_guard_addr").val().trim()
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("user inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Data Inserted Successfully!",
                        icon: "success",
                    }).then(()=>{
                        location.reload();
                    })
                }
                else if (data.includes("user already exists")) {
                    swal({
                        title: "Warning!",
                        text: "User Already Exists!!",
                        icon: "warning",
                    });
                }
                else if (data.includes("one of the field is empty")) {
                    swal({
                        title: "Failed!",
                        text: "One of the field is empty!",
                        icon: "error",
                    });
                }
                else {
                    swal({
                        title: "Failed!",
                        text: "Sorry for inconvenience!",
                        icon: "error",
                    });
                }
            }
        });
    });


    // fetching userid for searching operation here
    // $.ajax({
    //     method: 'post',
    //     url: 'pythonfile/user.py',
    //     data: {
    //         what: "fetchuserid",
    //     },
    //     success: function (data) {
    //         console.log(data)
    //         $("#userid").append(data)
    //     }
    // });


    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fetch_user_conditions",
                userid: $('#userid').val(),
                username: $('#username').val().trim(),
                mob_no: $('#mob_no').val().trim(),
                fname: $('#fname').val().trim(),
                mname: $('#mname').val().trim(),
                aadharno: $('#aadharno').val().trim(),
                bloodgrp: $('#bloodgrp').val(),
            },
            success: function (data) {
                console.log(data);

                if (data.includes("please select one field")) {
                    swal({
                        title: "Failed!",
                        text: "Please select atleast one field !!",
                        icon: "error",
                    });
                } else if (data.includes("product details fetched successfully")) {
                    $('#table-container').html(data)

                } else if (data.includes("no data available")) {
                    swal({
                        title: "Failed!",
                        text: "No data available",
                        icon: "error",
                    });
                }


                // if user click on delete button
                $(".del").on("click", function () {
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    console.log(uid);

                    swal({
                        title: "Are you sure?",
                        text: "Once deleted, you will not be able to recover this data!",
                        icon: "warning",
                        buttons: true,
                        dangerMode: true,
                    })
                        .then((willDelete) => {
                            if (willDelete) {
                                $.ajax({
                                    method: 'post',
                                    url: 'pythonfile/user.py',
                                    data: {
                                        what: "deleteuser",
                                        userid: uid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("user deleted successfully")) {

                                            swal("Yeah! Your data has been deleted!", {
                                                icon: "success",
                                            });

                                        } else {
                                            swal({
                                                title: "Failed!",
                                                text: "unable to delete somethings error!",
                                                icon: "error",
                                            });
                                        }
                                    },
                                });
                                $(this).closest('tr').remove();
                            } else {
                                swal("Your data is safe!", { icon: "success" });
                            }
                        });
                });

                $("#edit").on("click", function () {
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    sessionStorage.setItem('user_details',uid);
                    location.href='user.html';
                    console.log(uid);
                });



            },
        });
    });





});