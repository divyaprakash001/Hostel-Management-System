
$(document).ready(function () {

    $("#search_user").on("click",function(e){
        e.preventDefault();
        window.location.href = "Roomallocationservice.html";
    })

    
    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="Roomallocation.html";
    })


    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });


    // fetching room id
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
                $('#roomid').html(data_val[0]);
                $('#us_brow').html(data_val[4].trim());
            }
            else{
                swal('Warning','Please Do One Entry In Room Details and User Details!!','warning')
            }
        }
    });


    $("#userid").change(function () {
        // e.preventDefault();

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "checkuserid",
                userid: $("#userid").val().trim()
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



    $("#room_alloc_submit").on("click", function (e) {
        e.preventDefault();


        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "room_allocation",
                room_no: $("#roomid").val().trim(),
                userid: $('#userid').val().trim(),
                checkin: $("#checkin").val().trim(),
                checkout: $("#checkout").val().trim(),
                status: $("#status").val().trim(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("room allocated successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Room allocated Successfully!",
                        icon: "success",
                    })
                    .then((value)=>{
                        location.reload();
                    })
                }
                else if (data.includes("already exists!!")) {
                    swal({
                        title: "Warning!",
                        text: "Room Allocated already for this room number and user id!!",
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
                else if (data.includes("userid doesnot exists")) {
                    swal({
                        title: "Failed!",
                        text: "User Id doesn't exists!",
                        icon: "error",
                    });
                }else {
                    swal({
                        title: "Failed!",
                        text: "Sorry for inconvenience!",
                        icon: "error",
                    });
                }
            }
        });


    });




    // performing search operation


    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fetch_room_allocation_conditions",
                roomid: $('#roomid').val().trim(),
                userid: $('#userid').val().trim(),
                checkin: $('#checkin').val().trim(),
                checkout: $('#checkout').val().trim(),
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
                } else if (data.includes("room allocation fetched successfully")) {
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
                    let raid = $(this).closest('tr').children('td:first-child').text();
                    console.log(raid);

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
                                        what: "deleteroomalloc",
                                        roomid: raid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("room allocation deleted successfully")) {

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
                    let usid=$(this).closest('tr').children('td').eq(1).text();
                    sessionStorage.setItem('room_allocate',rid);
                    sessionStorage.setItem('room_allocate_us',usid);
                    location.href='Roomallocation.html';
                });
            },
        });
    });
});