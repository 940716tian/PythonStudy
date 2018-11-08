$(function () {
    $("#myform ").submit(function () {
        // 拿到用户名 密码 确认密码
        var name = $("#uid").val();
        var pwd = $("#u_pwd").val();
        var confirm_pwd = $("#u_confirm_pwd").val();

        // 判断用户名长度
        if (name.length <3) {
            alert("用户名过短");
        // 阻止提交
            return false;
        }
        //  判断密码长度
        if (pwd.length<3) {
            alert("密码过短");
            return false;
        }
        // 判断密码个确认密码
        if (pwd != confirm_pwd){
            alert("两次密码输入不一致");
            return false;
        }

         // 通过以上校验 我们加密密码和确认密码
        var enc_pwd  = md5(pwd);
        var enc_confirm_pwd = md5(confirm_pwd);

        // 将加密的值设置回去
        $("#u_pwd").val(enc_pwd);
        $("#u_confirm_pwd").val(enc_confirm_pwd);


    });

    $("#uid").change(function () {
        var uname = $("#uid").val();
        $.ajax({
            url:"/app10/check_uname",
            data:{
                uname:uname
            },
            method:"get",
            success:function (res) {
                // 提示用户
                if (res.code==1){
                    $("#uname_msg").html(res.msg);
                }else {
                    // 错误提示
                    alert(res.msg)
                }
            }
        })
    })
})