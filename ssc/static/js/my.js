function lastnameEnable(){                                                                               //first function
    $("#inputlast").prop("disabled", false);
}

function passwordEnable(){                                                                              //function II
    $("#inputpassword").prop("disabled",false)
}

$(document).ready(function(){                                                                           //only one time use ready function 
    
    $(document).on("change","#inputtext", lastnameEnable);                                              //code of first finction 
    $(document).on("change","#inputemail", passwordEnable);                                             //code of second function
});
