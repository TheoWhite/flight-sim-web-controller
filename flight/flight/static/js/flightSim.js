//Store the JSON data here
let output;

function loadLayout()
{
    CreateButton("Toggle Landing Gear","toggle_landing_gear");
    CreateButton("Toggle Landing Gear down","toggle_landing_gear_down");
    CreateLabel("Fuel state","fuel_state");
    CreateLabel("Altitude","plane_altitude");
    
    CreateLabel("x","Keyboard_label"); //Create but hide the label
    document.getElementById("Keyboard_label").style.visibility = "hidden";

}


function CreateButton(name,id)
{
    const div = document.createElement('div');
    const button = document.createElement('button');
    //Set the ID and some CSS
    button.innerText = name;
    button.id = id;
    div.style.paddingRight = "4%";
    //Append to Div
    div.appendChild(button);
    //Append to HTML 
    document.body.appendChild(div);
}

function CreateLabel(place_holder_text,id)
{
    const new_label = document.createElement('label');
    new_label.id = id;
    new_label.innerHTML = place_holder_text;
    new_label.style.paddingRight = "4%";
    document.body.appendChild(new_label);
}


function ModifyLabelText(new_text_value,id)
{
    //Use the ID of the label to modify the value of label
    const existing_label = document.getElementById(id);
    existing_label.innerHTML = new_text_value;
}


loadLayout();


//Handle the Get request
function getUserData() {
    jQuery.ajax({
        url: "/flightdata",
        type: 'GET',
        async: false,
        success: function(data) {
            ret = JSON.parse(data)
            output = ret
        }
    });
}

//Get token 

function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue && cookieValue[1];
  }

//Handle the POST request

function sendPOSTRequest(req) {
    jQuery.ajax({
        url: "/flightdata",
        type: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(), // Include the CSRF token in the request headers
        },
        data: {input:req},
        async: false,
    });
}


//Handlers for the buttons that are clicked

jQuery(document).on('click','#toggle_landing_gear',function(){
    //Change the state of the landing gear on button press
    let req = {"gear":"0"};
    sendPOSTRequest(req);
});

jQuery(document).on('click','#toggle_landing_gear_down',function(){
    //Change the state of the landing gear on button press
    let req = {"gear":"1"}
    sendPOSTRequest(req);
});

$('#keyboard').change(function() {
    var x=$("#keyboard").is(":checked");
    let p = x? 1:0;
    document.getElementById("Keyboard_label").style.visibility = "visible";
    ModifyLabelText(p,"Keyboard_label");

    let req = {"keyboard_value":p};
    
    sendPOSTRequest(req);
    //$('#keyboard').val(this.checked);  //Used to set the value       
});