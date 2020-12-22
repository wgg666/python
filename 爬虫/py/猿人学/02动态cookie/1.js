function setcookie() {
    let uqiop_date = new Date();//Wed Dec 16 2020 12:50:26 GMT+0800 (中国标准时间)
    //时间戳+18000000
    // new Date().getTime() + 18000000
    uqiop_date.setTime(uqiop_date.getTime() + 5* 60 * 60 * 1000);
    //'qpfccr=true;path=/;expires= + "Wed, 16 Dec 2020 09:55:00 GMT"
    // document.cookie = 'qpfccr=true;path=/;expires=' + uqiop_date.toUTCString();
    // document.cookie = 'no-alert=true; path=/'
    return 'qpfccr=true;path=/;expires=' + uqiop_date.toUTCString() + '; ' + 'no-alert=true; path=/; '
}
// if ($.cookie('no-alert') !== 'true'){
//     (function (){$('.alert_ban').click()})()
// }

console.log(setcookie())