$(function () {
    $("#submit").click(login);
})

function login() {

    // 拿到用户输入
    var name = $("#uid").val();
    var pwd = $("#u_pwd").val();
    // 校验数据格式
    if (name.length < 3) {
        alert("用户过短");
        return ;
    }
    if (pwd.length < 3) {
        alert("密码过短");
        return ;
    }
    // 给密码做MD5
    var enc_pwd = md5(pwd);
    // 发送Ajax请求
    $.ajax({
        url: "/app10/login",
        data: {
            "name": name,
            "pwd": enc_pwd,
        },
        method: "post",
        success: function (res) {
            // 如果成功 就跳转到mine.html
            if (res.code == 1) {
                window.open(res.data, target='_self');

            } else {
                // 如果失败 提示用户 alert
                alert(res.msg);
            }

        },
        error: function () {

        },
        complete:function () {
         // 请求完成是被执行
        }
    });
}

