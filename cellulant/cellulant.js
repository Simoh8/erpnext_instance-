// {% include "erpnext/accounts/doctype/payment_entry/payment_entry.js" %}

// frappe.ui.form.on('Payment Entry', {
//     mode_of_payment: function (frm) {
//         frm.toggle_display('credit_card_button');

//         if (frm.doc.mode_of_payment === "Credit Card") {
//             frm.add_custom_button('Send a Bank Request', function () {
//                 // Add your button's click event logic here
//                 console.log(frm.doc.party_name);
//                 frappe.prompt([
//                     {
//                         label: 'Student Name',
//                         fieldname: 'student_name',
//                         fieldtype: 'Data',
//                         reqd: 1,
//                         default: frm.doc.party_name
//                     },
//                     {
//                         label: 'Student ID',
//                         fieldname: 'student_id',
//                         fieldtype: 'Data',
//                         reqd: 1,
//                         default: frm.doc.party
//                     },
//                     {
//                         label: 'Card Number',
//                         fieldname: 'card_number',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
//                     {
//                         label: 'CCV',
//                         fieldname: 'ccv',
//                         fieldtype: 'Data',
//                         reqd: 1,
//                         maxlength: 3,

//                         onchange: function () {
//                             var ccvValue = this.get_value();
//                             if (ccvValue && ccvValue.length > 3) {
//                                 frappe.msgprint('CCV number should be maximum 3 digits.');
//                                 this.set_value('');
//                             }
//                         }
//                     },
//                     {
//                         label: 'Expiry Date',
//                         fieldname: 'expiry_date',
//                         fieldtype: 'Date',
//                         reqd: 1
//                     },

//                     {
//                         label: 'Cardholder Name',
//                         fieldname: 'cardholder_name',
//                         fieldtype: 'Data',
//                         reqd: 1,
//                     },
//                     {
//                         label: 'Enter Amount To Pay',
//                         fieldname: 'amount',
//                         fieldtype: 'Currency',
//                         reqd: 1,
//                         default: frm.doc.paid_amount
//                     }
//                 ], function (values) {
//                     // Handle payment logic here
//                     makePayment(values);
// 					console.log("this are the vales in the form");
//                 }, 'Send a Bank Request', 'Submit The Request');
//             });
// 			frm.remove_custom_button('Send Mobile Money Request');

//         } else if (frm.doc.mode_of_payment === 'Mobile Money') {
//             frm.add_custom_button('Send Mobile Money Request', function () {
//                 frappe.prompt([
//                     {
//                         label: 'Student Name',
//                         fieldname: 'student_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
// 					{
// 						label:'Student ID',
// 						fieldname:'Student_id',
// 						fieldtype:'Data',
// 						reqd:1,
// 						default:0
// 					},
// 					{
//                         label: 'Mobile Number',
//                         fieldname: 'mobile_number',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
// 					{
// 						label:'Amount To Pay',
// 						fieldname:'amount',
// 						fieldtype:'Data',
// 						reqd:1,
// 						default:0
// 					}
//                 ], function (values) {
//                     // Handle mobile money request logic here
//                     sendMobileMoneyRequest(values);
//                 }, 'Send Mobile Money Request', 'Submit The Request');
//             });
// 			frm.remove_custom_button('Send a Bank Request');


//         } else {
//             // If mode_of_payment is not "Credit Card" or "Mobile Money", remove the custom buttons
//             frm.remove_custom_button('Send a Bank Request');
//             frm.remove_custom_button('Send Mobile Money Request');
//         }
//     }
// });
