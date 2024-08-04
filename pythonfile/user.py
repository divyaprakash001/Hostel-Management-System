#! C:\Users\ASUS\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
# print()
import cgi
# import cgitb
import mysql.connector


con = mysql.connector.connect(host='localhost', user='hostel', passwd='data73063',database='hostel')
# print(con)
cur=con.cursor()
# print(cur)
f=cgi.FieldStorage()
flaguser = False
# print("jhj")
what = f.getvalue("what")
if(what == "user_details_insertion"):
    try:
        user_id = f.getvalue("emp_id")
        user_name = f.getvalue("emp_name")
        user_contact = f.getvalue("emp_contact")
        user_gender = f.getvalue("emp_gender")
        user_dob = f.getvalue("emp_dob")
        user_blood = f.getvalue("emp_blood")
        user_father = f.getvalue("emp_father")
        user_mother = f.getvalue("emp_mother")
        user_par_contact = f.getvalue("emp_par_contact")
        user_photo = f.getvalue("emp_photo")
        user_aadhar = f.getvalue("emp_aadhar")
        user_street = f.getvalue("emp_street")
        user_dist_state = f.getvalue("emp_dist_state")
        user_pincode = f.getvalue("emp_pincode")
        user_local_guard = f.getvalue("emp_local_guard")
        user_local_guard_cont = f.getvalue("emp_local_guard_cont")
        user_local_guard_addr = f.getvalue("emp_local_guard_addr")

        if( user_name != None and user_contact != None and user_dob != None
        and user_gender != None and user_dob != None and user_blood != None
        and user_father != None and user_mother != None and user_par_contact != None
        and user_photo != None and user_aadhar != None and user_street != None 
        and user_dist_state != None and user_pincode != None and user_local_guard != None and
        user_local_guard_cont != None and user_local_guard_addr != None):
            cur.execute(f'select * from user_info where userid="{user_id}"')
            if cur.fetchall()==[]:
                user_insert_query = f"insert into user_info (userid,username,user_cont,user_gender,user_dob,user_blood_grp,user_f_name,user_m_name,user_p_contact,user_pic,user_addhar,user_street,user_dstate,user_pin, user_local_guard,user_local_guard_cont, user_local_guard_add) values('{user_id}','{user_name}','{user_contact}','{user_gender}','{user_dob}','{user_blood}','{user_father}','{user_mother}','{user_par_contact}','{user_photo}','{user_aadhar}','{user_street}','{user_dist_state}','{user_pincode}','{user_local_guard}','{user_local_guard_cont}','{user_local_guard_addr}')"
                print(user_insert_query)
                cur.execute(user_insert_query)
                print("yaha")
                con.commit()
                print("user inserted successfully")
            else:
                print("user already exists")
        else:
            print("one of the field is empty")


    except Exception as e:
        print(e)

elif(what == "room_details_insertion"):
    try:
        room_no = f.getvalue("room_no")
        room_type = f.getvalue("room_type")
        total_bed = f.getvalue("total_bed")
        status = f.getvalue("status")

        if(room_no != None and room_type != None and total_bed != None and status != None):
            cur.execute(f"select * from room_details where room_no={room_no}")
            if cur.fetchall()==[]:
                room_details_insert = f"insert into room_details (room_no, room_type, total_bed, status) values('{room_no}','{room_type}','{total_bed}','{status}')"
                cur.execute(room_details_insert)
                con.commit()
                print("room details inserted successfully")
            else:
                print('Room Number Already Exists!!')
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)

elif(what=="fetchroomid"):
    try:
        cur.execute("select distinct room_no,room_type,total_bed,status from room_details")
        res = cur.fetchall()
        if res != []:
            room_no=set()
            room_type=set()
            total_bed=set()
            status=set()
            for row in res:
                room_no.add(row[0])
                room_type.add(row[1])
                total_bed.add(row[2])
                status.add(row[3])
            print('<option value="">-- Select Room Id --</option>')
            for row in room_no:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Room Type --</option>')
            for row in room_type:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select No. Of Bed --</option>')
            for row in total_bed:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Room Status --</option>')
            for row in status:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            if f.getvalue('user') == 'Yes':
                cur.execute("select distinct userid from user_info")
                res = cur.fetchall()
                if res != []:
                    for row in res:
                        print(f"<option value='{row[0]}'>{row[0]}</option>")
                else:
                    print()
            print('all detail fetched!!')
        else:
            print()
    except Exception as e:
        print(e)

elif(what=="userserdata"):
    try:
        cur.execute("select distinct userid,user_blood_grp from user_info")
        res = cur.fetchall()
        if res != []:
            userid=set()
            bloodgrp=set()
            for row in res:
                userid.add(row[0])
                bloodgrp.add(row[1])
            print('<option value="">-- Select User Id --</option>')
            for row in userid:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Blood Group --</option>')
            for row in bloodgrp:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('all detail fetched!!')
        else:
            print()
    except Exception as e:
        print(e)

elif(what=="checkuserid"):
    userid = f.getvalue("userid")
    checkUsername = cur.execute(f"SELECT userid FROM user_info WHERE userid='{userid}'")
    res = cur.fetchall()
    if res == []:
        print('Userid doesnot exist')
        flaguser=False
    else:
        flaguser=True


elif(what == "room_allocation"):
    try:
        room_no = f.getvalue("room_no")
        userid = f.getvalue("userid")
        checkin = f.getvalue("checkin")
        checkout = f.getvalue("checkout")
        status = f.getvalue("status")

        if(room_no != None and userid != None  and checkin != None and checkout != None and status != None):
            cur.execute(f'select * from room_allocation where roomid="{room_no}" and userid="{userid}"')
            if cur.fetchall()==[]:
                room_allocation_insert = f"insert into room_allocation(roomid, userid,checkin,checkout,status) values('{room_no}','{userid}','{checkin}','{checkout}','{status}')"
                cur.execute(room_allocation_insert)
                con.commit()
                print("room allocated successfully")
            else:
                print('already exists!!')
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)

elif(what == "fee_details_insertion"):
    try:
        user_id = f.getvalue("user_id")
        fee_amount = f.getvalue("fee_amount")
        paydate = f.getvalue("paydate")
        paymode = f.getvalue("paymode")
        month_name = f.getvalue("month_name")
        status = f.getvalue("status")

        if(user_id != None and fee_amount != None and paydate != None and paymode != None and month_name != None and status != None):
            fee_insertion = f"insert into fee_details(userid,fee_amount,pay_date,pay_mode,month_name,f_status) values('{user_id}','{fee_amount}','{paydate}','{paymode}','{month_name}','{status}')"
            cur.execute(fee_insertion)
            con.commit()
            print("fee inserted successfully")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)


elif(what == "rules_insertion"):
    try:
        user_id = f.getvalue("userid")
        rules_area = f.getvalue("rules_area")

        if(user_id != None and rules_area != None):
            cur.execute(f'select * from rules where userid="{user_id}"')
            if cur.fetchall() == []:
                rules_insertion = f"insert into rules(userid,rules) values('{user_id}','{rules_area}')"
                cur.execute(rules_insertion)
                con.commit()
                print("rules inserted successfully")
            else:
                print("already exists!!")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)

elif(what == "useridrules"):
    try:
        cur.execute("select distinct userid from rules")
        res = cur.fetchall()
        if res != []:
            print('<option value="">-- Select User Id --</option>')
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
            print('&&')
            print('all detail fetched!!')
        else:
            print()
    except Exception as e:
        print(e)
elif(what == "useridrulessearch"):
    try:
        userid = f.getvalue("userid")
        if userid:
            cur.execute(f'select * from rules where userid="{userid}"')
            srr = cur.fetchall()
            if srr != []:
                # print("<br>yes")
                print("<table style='width:100%;'><thead>")
                print("<tr>")
                print("<th>User ID</th>")
                print("<th>Rules Details</th>")
                print("<th colspan='2' style='text-align:center;'>Action</th>")
                print("</tr></thead><tbody>")
                for row in srr:
                    print("<tr>")
                    print(f'<td>{row[0]}</td>')
                    print(f'<td>{row[1]}</td>')
                    print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" style=\"color: green;cursor:pointer;\"></i></td>")
                    print(f"<td><i class='fa-solid fa-trash-can fa-xl del' style=\"color: red;cursor:pointer;\"></i></td>")
                    print("</tr>")
                print("</tbody></table>")
                print('<p style="display:none;">rules fetched successfully</p>')
            else:
                print("no data available")
        else:
            print('please select one field')
    except Exception as e:
        print(e)
elif (what == 'deleterulesuser'):
    try:
        userid = f.getvalue("userid")
        delete_room_query = f"delete from rules where userid = '{userid}'"
        cur.execute(delete_room_query)
        con.commit()
        print("ruleuser deleted successfully")
    except Exception as e:
        print(e)
        
elif(what == "fetchForRulesUpdate"):
    # print(what)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_for_upd_room = f"select * from rules where userid='{userid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print(*res[0],sep='&&')
                print('&&data fetching successfully!!')
            else:
                print("no data available")
    except Exception as e:
        print(e)  

elif(what == "savetheRuleupdate"):
    try:
        userid = f.getvalue("userid")
        rules = f.getvalue("rules")
        if( userid != None and rules != None):
            saveRoomUpdate_query = f"update rules SET rules = '{rules}' where userid = '{userid}'"
            cur.execute(saveRoomUpdate_query)
            con.commit()
            print("ruleuser successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)
                
elif(what=="fetchuserid"):
    try:
        cur.execute("select distinct userid from user_info")
        res = cur.fetchall()
        if res != []:
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print(e)


# fetching data on click of search button or searching data
elif(what == "fetch_user_conditions"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        username = f.getvalue("username")
        mob_no = f.getvalue("mob_no")
        fname = f.getvalue("fname")
        mname = f.getvalue("mname")
        aadharno = f.getvalue("aadharno")
        bloodgrp = f.getvalue("bloodgrp")
        

        # Construct conditions for the SQL query
        conditions = []
        if userid != None:
            conditions.append(f"userid = '{userid}'")
        if username is not None:
            conditions.append(f"username = '{username}'")
        if mob_no is not None:
            conditions.append(f"user_cont = '{mob_no}'")
        if fname is not None:
            conditions.append(f"user_f_name >= '{fname}'")
        if mname is not None:
            conditions.append(f"user_m_name < '{mname}'")
        if aadharno != None:
            conditions.append(f"user_addhar = '{aadharno}'")
        if bloodgrp is not None:
            conditions.append(f"user_blood_grp >= '{bloodgrp}'")

        # Construct the SQL query
        fetch_user_query = "SELECT * FROM user_info"
        if conditions:
            fetch_user_query += " WHERE " + " AND ".join(conditions)
            cur.execute(fetch_user_query)
            srr = cur.fetchall()
            if srr != []:
                # print("<br>yes")
                print("<table style='width:100%' id='myTable'><thead>")
                print("<tr>")
                print("<th>User&nbsp;Id</th>")
                print("<th>User&nbsp;Name</th>")
                print("<th>User&nbsp;Contact</th>")
                print("<th>Gender</th>")
                print("<th>DOB</th>")
                print("<th>Blood&nbsp;Group</th>")
                print("<th>Father's&nbsp;Name</th>")
                print("<th>Mother's&nbsp;Name</th>")
                print("<th>Parent&nbsp;Contact</th>")
                print("<th>Aadhar&nbsp;No.</th>")
                print("<th>Street</th>")
                print("<th>District,&nbsp;State</th>")
                print("<th>PinCode</th>")
                print("<th>Guardian&nbsp;Name</th>")
                print("<th>Guardian&nbsp;Number</th>")
                print("<th>Guardian&nbsp;Address</th>")
                print("<th>User&nbsp;Pic</th>")
                # print("<th>Size</th>")
                print("<th colspan='2' style='text-align:center;'>Action</th>")
                print("</tr></thead><tbody>")
                for row in srr:
                    # print(row)
                    print("<tr>")
                    print(f'<td>{row[0]}</td>')
                    print(f'<td>{row[1]}</td>')
                    print(f'<td>{row[2]}</td>')
                    print(f'<td>{row[3]}</td>')
                    print(f'<td>{row[4]}</td>')
                    print(f'<td>{row[5]}</td>')
                    print(f'<td>{row[6]}</td>')
                    print(f'<td>{row[7]}</td>')
                    print(f'<td>{row[8]}</td>')
                    print(f'<td>{row[10]}</td>')
                    print(f'<td>{row[11]}</td>')
                    print(f'<td>{row[12]}</td>')
                    print(f'<td>{row[13]}</td>')
                    print(f'<td>{row[15]}</td>')
                    print(f'<td>{row[16]}</td>')
                    print(f'<td>{row[14]}</td>')
                    print(f'<td><a href="{row[9].decode()}" class="view-link">view</a></td>')
                    print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" style='color:green;cursor:pointer;'></i></td>")
                    print(f"<td><i class='fa-solid fa-trash-can fa-xl del' style='color:red;cursor:pointer;'></i></td>")
                    print("</tr>")
                print("</tbody></table>")
                print("<p style='display:none;'>product details fetched successfully</p>")
            else:
                # print("no")
                print("no data available")
        else:
            print('please select one field')
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteuser"):
    try:
        user_id = f.getvalue("userid")
        # print(prod_id + " have gotten")
        delete_user_query = f"delete from user_info where userid = '{user_id}'"
        cur.execute(delete_user_query)
        con.commit()
        print("user deleted successfully")
    except Exception as e:
        print(e)


elif(what == "fetch_room_conditions"):
    # print(d)
    try:
        room_no = f.getvalue("room_no")
        roomtype = f.getvalue("roomtype")
        total_bed = f.getvalue("total_bed")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if room_no != None:
            conditions.append(f"room_no = '{room_no}'")
        if roomtype is not None:
            conditions.append(f"room_type = '{roomtype}'")
        if total_bed is not None:
            conditions.append(f"total_bed <= '{total_bed}'")
        if status is not None:
            conditions.append(f"status = '{status}'")
        

        # Construct the SQL query
        fetch_room_query = "SELECT * FROM room_details"
        if conditions:
            fetch_room_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_room_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table style='width:100%;'><thead>")
            print("<tr>")
            print("<th>Room No</th>")
            print("<th>Room Type</th>")
            print("<th>Total Bed</th>")
            print("<th>Status</th>")
            print("<th colspan='2' style='text-align:center;'>Action</th>")
            print("</tr></thead><tbody>")
            for row in srr:
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" style=\"color: green;cursor:pointer;\"></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del' style=\"color: red;cursor:pointer;\"></i></td>")
                print("</tr>")
            print("</tbody></table>")
            print('<p style="display:none;">room details fetched successfully</p>')
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteroom"):
    try:
        roomid = f.getvalue("roomno")
        delete_room_query = f"delete from room_details where room_no = '{roomid}'"
        print(delete_room_query)
        cur.execute(delete_room_query)
        con.commit()
        print("room deleted successfully")
    except Exception as e:
        print(e)

# fetching data on click of search button or searching data
elif(what == "fetch_room_allocation_conditions"):
    # print(d)
    try:
        roomid = f.getvalue("roomid")
        userid = f.getvalue("userid")
        checkin = f.getvalue("checkin")
        checkout = f.getvalue("checkout")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if roomid != None:
            conditions.append(f"roomid = '{roomid}'")
        if userid is not None:
            conditions.append(f"userid = '{userid}'")
        if checkin is not None:
            conditions.append(f"checkin = '{checkin}'")
        if checkout is not None:
            conditions.append(f"checkout = '{checkout}'")
        if status is not None:
            conditions.append(f"status = '{status}'")
        

        # Construct the SQL query
        fetch_room_alloc_query = "SELECT * FROM room_allocation"
        if conditions:
            fetch_room_alloc_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_room_alloc_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table style=\"width:100%\"><thead>")
            print("<tr>")
            print("<th>Room No</th>")
            print("<th>User Id</th>")
            print("<th>Checkin</th>")
            print("<th>Checkout</th>")
            print("<th>Status</th>")
            print("<th colspan='2' style='text-align:center;'>Action</th>")
            print("</tr></thead><tbody>")
            for row in srr:
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" style='color:green;cursor:pointer;'></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del' style='color:red;cursor:pointer;'></i></td>")
                print("</tr>")
            print("</tbody></table>")
            print("<p style='display:none;'>room allocation fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteroomalloc"):
    try:
        roomid = f.getvalue("roomid")
        delete_room_alloc_query = f"delete from room_allocation where roomid = '{roomid}'"
        print(delete_room_alloc_query)
        cur.execute(delete_room_alloc_query)
        con.commit()
        print("room allocation deleted successfully")
    except Exception as e:
        print(e)

elif(what == 'allfeeinput'):
    try:
        cur.execute("select * from fee_details")
        res = cur.fetchall()
        if res != []:
            userid=set()
            month_name=set()
            fstatus=set()
            paymode=set()
            for row in res:
                userid.add(row[1])
                paymode.add(row[4])
                month_name.add(row[5])
                fstatus.add(row[6])
            print('<option value="">-- Select User Id --</option>')
            for row in userid:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Payment Mode --</option>')
            for row in paymode:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Payment Month --</option>')
            for row in month_name:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Payment Status --</option>')
            for row in fstatus:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('all detail fetched!!')
        else:
            print()
    except Exception as e:
        print(e)
# fetching data on click of search button or searching data
elif(what == "fee_details_condtions"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        fee_amt = f.getvalue("fee_amt")
        paydate = f.getvalue("paydate")
        pay_mode = f.getvalue("pay_mode")
        month_name = f.getvalue("month_name")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if userid != None:
            conditions.append(f"userid = '{userid}'")
        if fee_amt is not None:
            conditions.append(f"fee_amount = '{fee_amt}'")
        if paydate is not None:
            conditions.append(f"pay_date = '{paydate}'")
        if pay_mode is not None:
            conditions.append(f"pay_mode = '{pay_mode}'")
        if month_name is not None:
            conditions.append(f"month_name = '{month_name}'")
        if status is not None:
            conditions.append(f"f_status = '{status}'")
        

        # Construct the SQL query
        fetch_feedetails_query = "SELECT * FROM fee_details"
        if conditions:
            fetch_feedetails_query += " WHERE " + " AND ".join(conditions)
            cur.execute(fetch_feedetails_query)
            srr = cur.fetchall()
            if srr != []:
                # print("<br>yes")
                print("<table style='width:100%'><thead>")
                print("<tr>")
                print("<th hidden>SN.</th>")
                print("<th>User Id</th>")
                print("<th>Fee Amount</th>")
                print("<th>Payment Date</th>")
                print("<th>Payment Mode</th>")
                print("<th>Month Name</th>")
                print("<th>Payment Status</th>")
                print("<th colspan='2' style='text-align:center;'>Action</th>")
                print("</tr></thead><tbody>")
                for row in srr:
                    # print(row)
                    print("<tr>")
                    print(f'<td hidden>{row[0]}</td>')
                    print(f'<td>{row[1]}</td>')
                    print(f'<td>{row[2]}</td>')
                    print(f'<td>{row[3]}</td>')
                    print(f'<td>{row[4]}</td>')
                    print(f'<td>{row[5]}</td>')
                    print(f'<td>{row[6]}</td>')
                    
                    print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" style='color:green;cursor:pointer;'></i></td>")
                    print(f"<td><i class='fa-solid fa-trash-can fa-xl del' style='color:red;cursor:pointer;'></i></td>")
                    print("</tr>")
                print("</tbody></table>")
                print("<p style='display:none;'>fee details fetched successfully</p>")
            else:
                # print("no")
                print("no data available")
        else:
            print('please select one field')
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deletefee"):
    try:
        userid = f.getvalue("userid")
        delete_fee_query = f"delete from fee_details where id = '{userid}'"
        print(delete_fee_query)
        cur.execute(delete_fee_query)
        con.commit()
        print("room allocation deleted successfully")
    except Exception as e:
        print(e)

elif(what == "fetchForRoomUpdate"):
    # print(what)
    try:
        roomid = f.getvalue("roomid")
        # print(userid + " have gotten")
        if(roomid != None):
            fetch_for_upd_room = f"select * from room_details where room_no='{roomid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print(*res[0],sep='&&')
                print('&&data fetching successfully!!')
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheRoomupdate"):
    try:
        room_no = f.getvalue("room_no")
        room_type = f.getvalue("room_type")
        t_bed = f.getvalue("t_bed1")
        status = f.getvalue("status1")

        print(room_no,room_type,t_bed,status)
        
        if( room_type != None and t_bed != None and status != None):
            saveRoomUpdate_query = f"update room_details SET room_type = '{room_type}', total_bed = '{t_bed}',status = '{status}' where room_no = '{room_no}'"
            cur.execute(saveRoomUpdate_query)
            con.commit()
            print("room details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif(what == "fetchForRoomAllocUpdate"):
    # print(what)
    try:
        roomid = f.getvalue("roomid")
        userid = f.getvalue("userid")
        if(roomid != None):
            fetch_for_upd_room_alloc = f"select * from room_allocation where roomid='{roomid}' and userid='{userid}'"
            cur.execute(fetch_for_upd_room_alloc)
            res = cur.fetchall()
            if res != []:
                print(*res[0],sep='&&')
                print('&&data fetching successfully')
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheRoomAllocupdate"):
    try:
        roomid1 = f.getvalue("roomid1")
        userid1 = f.getvalue("userid1")
        checkin1 = f.getvalue("checkin1")
        checkout1 = f.getvalue("checkout1")
        status1 = f.getvalue("status1")

        print(roomid1,userid1,checkin1,checkout1,status1)
        
        if( roomid1 != None and userid1 != None and checkin1 != None and checkout1 != None and status1 != None):
            saveRoomAllocUpdate_query = f"update room_allocation SET checkin = '{checkin1}',checkout = '{checkout1}', status='{status1}' where roomid = '{roomid1}' and userid = '{userid1}'"
            cur.execute(saveRoomAllocUpdate_query)
            con.commit()
            print("room allocation details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif(what == "fetchFeeUpdate"):
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_for_upd_room = f"select * from fee_details where id='{userid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print(*res[0],sep='&&')
                print('&&data fetching successfully!!')
            else:
                print("no data available")
    except Exception as e:
        print(e)  

elif(what == "savetheFeeUpdate"):
    try:
        id = f.getvalue("id")
        userid1 = f.getvalue("userid1")
        fee_amt1 = f.getvalue("fee_amt1")
        paydate1 = f.getvalue("paydate1")
        paymode1 = f.getvalue("paymode1")
        month_name1 = f.getvalue("month_name1")
        status1 = f.getvalue("status1")

        
        if( userid1 != None and fee_amt1 != None and paydate1 != None and paymode1 != None and month_name1 and status1 != None):
            saveFeeUpd_query = f"update fee_details SET pay_date = '{paydate1}', pay_mode = '{paymode1}',month_name = '{month_name1}', f_status='{status1}', fee_amount='{fee_amt1}' where id = '{id}'"
            cur.execute(saveFeeUpd_query)
            con.commit()
            print("fee details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)


elif(what == "fetchUserUpdate"):
    # print(what)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_for_upd_room = f"select * from user_info where userid='{userid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print(*res[0],sep='&&')
                print('&&data fetching successfully!!')
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheUserUpdate"):
    try:
        user_id1 = f.getvalue("emp_id1")
        user_name1 = f.getvalue("emp_name1")
        user_contact1 = f.getvalue("emp_contact1")
        user_gender1 = f.getvalue("emp_gender1")
        user_dob1 = f.getvalue("emp_dob1")
        user_blood1 = f.getvalue("emp_blood1")
        user_father1 = f.getvalue("emp_father1")
        user_mother1 = f.getvalue("emp_mother1")
        user_par_contact1 = f.getvalue("emp_par_contact1")
        user_photo1 = f.getvalue("emp_photo1")
        user_aadhar1 = f.getvalue("emp_aadhar1")
        user_street1 = f.getvalue("emp_street1")
        user_dist_state1 = f.getvalue("emp_dist_state1")
        user_pincode1 = f.getvalue("emp_pincode1")
        user_local_guard1 = f.getvalue("emp_local_guard1")
        user_local_guard_cont1 = f.getvalue("emp_local_guard_cont1")
        user_local_guard_addr1 = f.getvalue("emp_local_guard_addr1")
        
        if( user_name1 != None and user_contact1 != None and user_dob1 != None
        and user_gender1 != None and user_dob1 != None and user_blood1 != None
        and user_father1 != None and user_mother1 != None and user_par_contact1 != None
        and user_aadhar1 != None and user_street1 != None 
        and user_dist_state1 != None and user_pincode1 != None and user_local_guard1 != None and
        user_local_guard_cont1 != None and user_local_guard_addr1 != None):
            
            # saveUserUpd_query = f"update user_info SET username = '{user_name1}', user_cont = '{user_contact1}',user_gender = '{user_gender1}', user_dob='{user_dob1}', user_blood_grp='{user_blood1}', user_f_name='{user_father1}', user_m_name='{user_mother1}', user_p_contact='{user_par_contact1}', user_pic='{user_photo1}' , user_addhar='{user_aadhar1}', user_street='{user_street1}', user_dstate='{user_dist_state1}', user_pin='{user_pincode1}', user_local_guard='{user_local_guard1}' , user_local_guard_cont='{user_local_guard_cont1}', user_local_guard_add='{user_local_guard_addr1}' where userid = '{user_id1}'"
            # cur.execute(saveUserUpd_query)
            # con.commit()
            saveUserUpd_query = """
                UPDATE user_info 
                SET username = %s, user_cont = %s, user_gender = %s, user_dob = %s, user_blood_grp = %s, 
                user_f_name = %s, user_m_name = %s, user_p_contact = %s, user_pic = %s, user_addhar = %s, 
                user_street = %s, user_dstate = %s, user_pin = %s, user_local_guard = %s, 
                user_local_guard_cont = %s, user_local_guard_add = %s 
                WHERE userid = %s
            """

            # Execute the query with the provided data
            cur.execute(saveUserUpd_query, (
                user_name1, user_contact1, user_gender1, user_dob1, user_blood1,
                user_father1, user_mother1, user_par_contact1, user_photo1,
                user_aadhar1, user_street1, user_dist_state1, user_pincode1,
                user_local_guard1, user_local_guard_cont1, user_local_guard_addr1,
                user_id1
            ))

            print("user details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif (what == 'roomallocationservice'):
    try:
        cur.execute("select distinct roomid,userid,status from room_allocation")
        res = cur.fetchall()
        if res != []:
            room_no=set()
            user_id=set()
            status=set()
            for row in res:
                room_no.add(row[0])
                user_id.add(row[1])
                status.add(row[2])
            print('<option value="">-- Select Room ID --</option>')
            for row in room_no:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select User ID --</option>')
            for row in user_id:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('<option value="">-- Select Room Status --</option>')
            for row in status:
                print(f"<option value='{row}'>{row}</option>")
            print('&&')
            print('all detail fetched!!')
        else:
            print()
    except Exception as e:
        print(e)