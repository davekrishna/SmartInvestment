
$(document).ready(function() {
  
    $("#fname").focusout(function(){
        var name=$("#fname").val();
        var re= /^[a-zA-Z]+$/;
        if(name == "")
        {
            alert("name field cannnot be empty");
        }
        else
        {
            if(!re.test(name))
            {
                alert('name can contain only letters');
            }
        }
    });

    $("#lname").focusout(function(){
        var name=$("#lfname").val();
        var re= /^[a-zA-Z]+$/;
        if(name == "")
        {
            alert("name field cannnot be empty");
        }
        else
        {
            if(!re.test(name))
            {
                alert('name can contain only letters');
            }
        }
    });

    $("#emailid").focusout(function(){
        var email=$("#emailid").val();
        var re =/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
        if(email=="")
        {
            alert("email id field cannnot be empty");
        }
        else
        {
            if(!email.match(re))
            {
                alert("email id format is not proper");
            }
        }
    });

    $("#c_name").focusout(function(){
        var name=$("#c_name").val();
        var re= /^[a-zA-Z]+$/;
        if(name == "")
        {
            alert("name field cannnot be empty");
        }
        else
        {
            if(!re.test(name))
            {
                alert('name can contain only letters');
            }
        }
    });

    $("#c_email").focusout(function(){
        var email=$("#c_email").val();
        var re =/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
        if(email=="")
        {
            alert("email id field cannnot be empty");
        }
        else
        {
            if(!email.match(re))
            {
                alert("email id format is not proper");
            }
        }
    });

    $("#r_name").focusout(function(){
        var name=$("#r_name").val();
        var re= /^[a-zA-Z]+$/;
        if(name == "")
        {
            alert("name field cannnot be empty");
        }
        else
        {
            if(!re.test(name))
            {
                alert('name can contain only letters');
            }
        }
    });

    $("#r_email").focusout(function(){
        var email=$("#r_email").val();
        var re =/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
        if(email=="")
        {
            alert("email id field cannnot be empty");
        }
        else
        {
            if(!email.match(re))
            {
                alert("email id format is not proper");
            }
        }
    });

});
