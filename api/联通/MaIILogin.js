/* 
jQuery.extend({
      cache:{},
      uuid:0,
      expando:"jQuery"+(jQuery.fn.jquery+Math.random()).replace(/\D/g,"")
})
*/
var expando = "jQuery"+('1.7.2'+Math.random()).replace(/\D/g,"")
var RSAUtils = {};
//加密指数 解密组件 模数
var RSAKeyPair = function(encryptionExponent, decryptionExponent, modulus) {
    var $dmath = RSAUtils;
    this.e = $dmath.biFromHex(encryptionExponent);
    this.d = $dmath.biFromHex(decryptionExponent);
    this.m = $dmath.biFromHex(modulus);
    // We can do two bytes per digit, so
    // chunkSize = 2 * (number of digits in modulus - 1).
    // Since biHighIndex returns the high index, not the number of digits, 1 has
    // already been subtracted.
    this.chunkSize = 2 * $dmath.biHighIndex(this.m);
    this.radix = 16;
    this.barrett = new $w.BarrettMu(this.m);
};
RSAUtils.getKeyPair = function(encryptionExponent, decryptionExponent, modulus) {
    return new RSAKeyPair(encryptionExponent,decryptionExponent,modulus);
}

var key = RSAUtils.getKeyPair('11', '', '82fd84c464ab864897660ec64bafc32b998b60d5713dd57177820da7cf2409836b4506aa5c2b2943e701b6810df16da0b47e96274765aaf2d72152c5ca76d796756ec8c496cf4365c350c52312368e0c8c5504a14b1122bbde9c0f05627f33eb05ad52ea1f2c8ca7cf6a68e4ee9eee6b45773dc11fe830778202c8209d2ffaab');
params.password = RSAUtils.encryptedString(key, '520886'.trim());
