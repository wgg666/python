var rsa = function(arg) {
    setMaxDigits(130)
    var PublicExponent = "10001";
    var modulus = "";
    var key = new RSAKeyPair(PublicExponent,'',modulus);
    return encryptedString(key, arg);
} 
console.log(rsa('123456'))