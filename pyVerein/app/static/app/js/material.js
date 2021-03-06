var drawer;
$(document).ready(function () {
// Top App Bar
const topAppBarElement = document.querySelector('.mdc-top-app-bar');
if (topAppBarElement != null){
    const topAppBar = new mdc.topAppBar.MDCTopAppBar(topAppBarElement);
}

// Account-Menu
var account_menu_sel = document.querySelector('#account-menu');
if (account_menu_sel != null){
    let menu = mdc.menu.MDCMenu.attachTo(account_menu_sel);
    document.querySelector('a.account-menu').onclick = function() {
        menu.open = !menu.open;
    }
}
// Drawer
var drawer_sel = document.querySelector('.mdc-drawer--modal');
if (drawer_sel != null){
    drawer = mdc.drawer.MDCDrawer.attachTo(drawer_sel);
    document.querySelector('.menu').addEventListener('click', () => drawer.open = !drawer.open);
}
// Floating action button
var fabRipple_sel = document.querySelectorAll('.mdc-fab');
if (fabRipple_sel != null){
    fabRipple_sel.forEach(function(val){
        mdc.ripple.MDCRipple.attachTo(val);
    });
}

// Lineripple
var ripple_sel = document.querySelectorAll('.mdc-line-ripple');
if (ripple_sel != null){
    ripple_sel.forEach(function (val){
        mdc.lineRipple.MDCLineRipple.attachTo(val);
    })
}

// Textfield
var textfield_sel = document.querySelectorAll('.mdc-text-field');
if (textfield_sel != null){
    textfield_sel.forEach(function (val){
        mdc.textField.MDCTextField.attachTo(val);
    })

}

// Textfield helper text
// var helper_text_sel = document.querySelectorAll('.mdc-text-field-helper-text');
// if (helper_text_sel != null){
//     helper_text_sel.forEach(function(val){
//         mdc.textField.MDCTextFieldHelperText.attachTo(val);
//     });
// }

// List-ripple
var list_ripple_sel = document.querySelectorAll('.mdc-list-item');
if (list_ripple_sel != null){
    list_ripple_sel.forEach(function(val){
        mdc.ripple.MDCRipple.attachTo(val);
    });
}


// Button-ripple
var button_ripple_sel = document.querySelectorAll('.mdc-button');
if (button_ripple_sel != null){
    button_ripple_sel.forEach(function(val){
        mdc.ripple.MDCRipple.attachTo(val);
    });
}

// Radio
var formField_sel = document.querySelectorAll('.mdc-form-field');
if (formField_sel != null){
    formField_sel.forEach(function (ff){
        var radio_sel = ff.querySelector('.mdc-radio');
        if (radio_sel != null){
            ff.input = new mdc.radio.MDCRadio(radio_sel);
        }
    })
}

// Select
var select_sel = document.querySelectorAll('.mdc-select');
if (select_sel != null){
    select_sel.forEach(function(val){
        mdc.select.MDCSelect.attachTo(val);
    });
}

// checkbox
var formField_sel = document.querySelectorAll('.mdc-form-field');
if (formField_sel != null){
    formField_sel.forEach(function (ff){
        var checkbox_sel = ff.querySelector('.mdc-checkbox');
        if (checkbox_sel != null){
            ff.input = new mdc.checkbox.MDCCheckbox(checkbox_sel);
        }
    })
}
});