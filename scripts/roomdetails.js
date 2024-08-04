
$(document).ready(function () {

    $("#search_user").on("click",function(e){
        e.preventDefault();
        window.location.href = "Roomservice.html";
    })

    
    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="Roomdetail.html";
    })
    
    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });




    $("#room_submit").on("click", function (e) {
        e.preventDefault();
        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "room_details_insertion",
                room_no: $("#room_no").val().trim(),
                room_type: $("#room_type").val().trim(),
                total_bed: $("#t_bed").val().trim(),
                status: $("#status_ent").val().trim(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("room details inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Data Inserted Successfully!",
                        icon: "success",
                    })
                    .then((willDelete) => {
                        if (willDelete) {
                            location.reload();
                        }
                    });

                    
                } 
                else if (data.includes("Room Number Already Exists!!")) {
                    swal({
                        title: "Failed!",
                        text: "Room Number Already Exists!!",
                        icon: "error",
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



    // fetching roomid for searching operation here
    $.ajax({
        method: 'post',
        url: 'pythonfile/user.py',
        data: {
            what: "fetchroomid",
        },
        success: function (data) {
            console.log(data)
            if (data.includes('all detail fetched!!')){
                var data_val=data.split('&&');
                $('#roomno').html(data_val[0]);
                $('#roomtype').html(data_val[1]);
                $('#t_bed').html(data_val[2]);
                $('#status').html(data_val[3]);
            }
            else{
                swal('Warning','Please Do One Entry In Room Details!!','warning')
            }
        }
    });


    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fetch_room_conditions",
                room_no: $('#roomno').val().trim(),
                roomtype: $('#roomtype').val().trim(),
                total_bed: $('#t_bed').val().trim(),
                status: $('#status').val().trim(),
            },
            success: function (data) {
                console.log(data);
                if (data.includes("please select one field")) {
                    $('.below_card').css({ "display": "none" })
                    swal({
                        title: "Failed!",
                        text: "please select atleast one field",
                        icon: "error",
                    });
                } else if (data.includes("room details fetched successfully")) {
                    $('.below_card').css({ "display": "block" })
                    $('#table-container').html(data)

                } else if (data.includes("no data available")) {
                    $('.below_card').css({ "display": "none" })
                    swal({
                        title: "Failed!",
                        text: "no data available",
                        icon: "error",
                    });
                }


                // if user click on delete button
                $(".del").on("click", function () {
                    let rid = $(this).closest('tr').children('td:first-child').text();
                    console.log(rid);

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
                                        what: "deleteroom",
                                        roomno: rid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("room deleted successfully")) {

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
                    let rid = $(this).closest('tr').children('td:first-child').text();
                    sessionStorage.setItem('room_id',rid);
                    location.href='Roomdetail.html';
                    console.log(rid);
                });
            },
        });
    });


    // docu


});