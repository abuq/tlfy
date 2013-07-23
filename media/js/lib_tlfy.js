$(function() {
	$.datepicker.regional['zh-CN'] = { 
        clearText: '清除', 
        clearStatus: '清除已选日期', 
        closeText: '关闭', 
        closeStatus: '不改变当前选择', 
        prevText: '<上月', 
        prevStatus: '显示上月', 
        prevBigText: '<<', 
        prevBigStatus: '显示上一年', 
        nextText: '下月>', 
        nextStatus: '显示下月', 
        nextBigText: '>>', 
        nextBigStatus: '显示下一年', 
        currentText: '今天', 
        currentStatus: '显示本月', 
        monthNames: ['一月','二月','三月','四月','五月','六月', '七月','八月','九月','十月','十一月','十二月'], 
        monthNamesShort: ['一','二','三','四','五','六', '七','八','九','十','十一','十二'], 
        monthStatus: '选择月份', 
        yearStatus: '选择年份', 
        weekHeader: '周', 
        weekStatus: '年内周次', 
        dayNames: ['星期日','星期一','星期二','星期三','星期四','星期五','星期六'], 
        dayNamesShort: ['周日','周一','周二','周三','周四','周五','周六'], 
        dayNamesMin: ['日','一','二','三','四','五','六'], 
        dayStatus: '设置 DD 为一周起始', 
        dateStatus: '选择 m月 d日, DD', 
        dateFormat: 'yy-mm-dd', 
        firstDay: 1, 
        initStatus: '请选择日期', 
        isRTL: false}; 
    $.datepicker.setDefaults($.datepicker.regional['zh-CN']); 
	set_inner_tip();
	set_is_num();
	
	$(".award-img-wrapper").mouseover(function(){
		
		$(this).next().next().show();
	}).mouseout(function(){
		$(this).next().next().hide();
	});

	$(".v").parent().mouseover(function(){
		$(this).find(".v").next().show();
	}).mouseout(function(){
		$(this).find(".v").next().hide();
	});
	//set_edit_btn();
});

function check_before_register()
{
	$(".error").html("");
	is_pwdc_valid($('#password_confirm').val());
	is_pwd_valid($('#password').val());
	is_email_valid($('#email').val());
	if($('#real_name').val() == "")
	{
		set_error("真实姓名不能为空", 1);
	}
	else
	{
		set_error("真实姓名不能为空", 0);
	}
	if($("#university").val() == "")
	{
		set_error("请选择您的学校", 1);
	}
	else
	{
		set_error("请选择您的学校", 0);
	}
	if($("input[@name=sex]:checked").val() != "0" && $("input[@name=sex]:checked").val() != "1")
	{
		set_error("请选择您的姓别", 1);
	}
	else
	{
		set_error("请选择您的性别", 0);
	}
	if($("#agreement").attr("checked") == true || $("#agreement").attr("checked") == "checked")
	{
		set_error("注册用户必须接受师兄帮帮忙网的服务条款", 0);
	}
	else
	{
		set_error("注册用户必须接受师兄帮帮忙网的服务条款", 1);
	}
	if($.trim($('.error').html()) == "")
	{
		return true;
	}
	else
	{
		return false;
	}
}

function check_before()
{
	$(".error").html("");
	if($("#agreement").attr("checked") == true || $("#agreement").attr("checked") == "checked")
	{
		set_error("注册用户必须接受INOOLD的服务条款", 0);
	}
	else
	{
		set_error("注册用户必须接受INOOLD的服务条款", 1);
	}
	if($.trim($('.error').html()) == "")
	{
		return true;
	}
	else
	{
		return false;
	}
}

function is_email_valid(str)
{
	re = /^([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	if (false == re.test(str))
	{
		set_error("电子邮箱地址有误",1);
	}
	else
	{
		set_error("电子邮箱地址有误",0);
	}
	return re.test(str); 
}
function is_pwd_valid(str)
{
	if(str.length < 6 || str.length > 20 )
	{
		set_error("密码长度有误(6-20个字符)",1);
	}
	else
	{
		set_error("密码长度有误(6-20个字符)",0);
	}
}
function is_pwdc_valid(str)
{
	pwd = $('#password').val();
	if(str != pwd)
	{
		set_error("两次输入密码不一致",1);
	}
	else
	{
		set_error("两次输入密码不一致",0);
	}
}
function set_error(str, flag)
{
	if(flag == 1)
	{
		$('.error').html(str).show();
		setInterval("$('.error').fadeOut(3000)", 3000);
	}
	else
	{
		if($('.error').html() == str)
		{
			$('.error').html("").hide();
		}
	}
}

function tag_get(obj)
{
	$.ajax({
		type : "GET",
		url : "/get_tags/",
		data : {},
		dataType :"html",
		success : function(data) {
			obj.find(".tag-item").remove();
			obj.append(data);
		}
	}); 
}
function tag_add_clicked(obj)
{
	tc = parseInt($('#tags_count').val());
	if(tc >= 8)
	{
		alert("您最多只能添加8个标签");
		return false;
	}
	obj.find('.tag-add-btn').remove();
	obj.append('<a class="pointer tag-del-btn" onclick="tag_del_clicked($(this).parent());"></a>');
	$('.tags-selected-div').append(obj);
	$('#tags_count').val(tc+1);	
}
function tag_del_clicked(obj)
{
	tc = parseInt($('#tags_count').val());
	if(tc > 0)
	{
		$('#tags_count').val(tc-1);	
	}
	obj.remove();
}
function tag_input_clicked()
{
	tc = parseInt($('#tags_count').val());
	v = $.trim($('#tag-input').val());
	if(v == "")
	{
		return false;
	}
	if(tc >= 8)
	{
		alert("您最多只能添加8个标签");
		return false;
	}
	obj = '<div class="tag-item">';
	obj = obj+'<span class="tag-name">'+$('#tag-input').val()+'</span>';
	obj = obj+'<a class="tag-del-btn pointer" onclick="tag_del_clicked($(this).parent());"></a>';
	obj = obj+'</div>';
	$('.tags-selected-div').append(obj);
	$('#tag-input').val('');
	$('#tags_count').val(tc+1);	
	
}
function tag_input_clicked_for_task(str)
{
	tc = parseInt($('#tags_count').val());
	str = $.trim(str);
	if(str == "")
	{
		return false;
	}
	if(tc >= 3)
	{
		alert("您最多只能添加3个标签");
		return false;
	}
	obj = '<div class="tag-item">';
	obj = obj+'<span class="tag-name">'+str+'</span>';
	obj = obj+'<a class="tag-del-btn pointer" onclick="tag_del_clicked($(this).parent());"></a>';
	obj = obj+'</div>';
	$('#tags').parent().append(obj);
	$('#tags').val('');
	$('#tags_count').val(tc+1);	
}
function tag_input_keydown(event)
{
	if(event.keyCode == 13)
	{
		tag_input_clicked();
		event.returnValue = false;
		event.preventDefault();
	}
}
function tag_input_keydown_for_task(event)
{
	if(event.keyCode == 13 || event.keyCode == 32)
	{
		tag_input_clicked_for_task($('#tags').val());
		event.returnValue = false;
		event.preventDefault();
	}
}
function fill_input_tags()
{
	v = "";
	$('.tags-selected-div .tag-name')
		.each(function(){v = v+$(this).html()+',';});
	$('#input-tags').val(v);
}
function set_inner_tip()
{
	$("[innertip]").each(function(){
		tip = $(this).attr('innertip');
		v = $(this).clone()
			.removeAttr('name')
			.removeAttr('id')
			.removeAttr('innertip')
			.attr('type','text')
			.val(tip).addClass('innertip');
		$(this).after(v).hide();
		$(this).next().focus(function(){
			$(this).hide();
			$(this).prev().show().focus();
		});
		$(this).blur(function(){
			if($.trim($(this).val()) == "")
			{
				$(this).hide().next().show();
			}
		});

		if($(this).val() != "")
		{
			$(this).show();
			$(this).next().hide();
		}
	});
	/*$("[innertip]").each(function(){
		tip = $(this).attr('innertip');
		$(this).val(tip);
		$(this).focus(function(){
			if($(this).val() == tip)
			{
				$(this).val("");
			}
		}).blur(function(){
			if($.trim($(this).val()) == "")
			{
				$(this).val(tip);
			}
		});
	});*/
}
function set_is_num()
{
	$("[onlynum]").each(function(){
		$(this).keydown(function(event){
			keyCode = event.keyCode;
			if ((keyCode >= 48 && keyCode <= 57) || (keyCode >= 96 && keyCode <= 105) ||keyCode==8)
			{
				event.returnValue = true;
			} else {
				event.returnValue = false;
				event.preventDefault();//for firefox
			} 
		});
	});
}
function get_check_code(obj)
{
	obj.html("<img src='/getcode/?r="+Math.random()+"'>");
}
function replyTo(obj)
{
	name = obj.parent().find(".name").html();
	$("#to_id").val(obj.next().val());
	$("#comment-content").focus().val("对"+name+"说：");
}
function commit_comment()
{
	if($.trim($("#comment-content").val()) == "")
	{
		alert('评论内容不能为空');
		$("#comment-content").focus();
	}
	else
	{
		$("#comment-content").val($.trim($("#comment-content").val()));
		$("#comment-form").submit();
	}
}
function ctrl_enter(event)
{
	if(event.ctrlKey == true && event.keyCode == 13)
	{
		commit_comment();
	}
	check_textarea_length(event);
}
function check_textarea_length(event)
{
	if($('#comment-content').val().length >= 100 && event.keyCode!=8)
	{
		event.returnValue = false;
		event.preventDefault();
	}
}
function textarea_length(event, val)
{
	if(val.length >= 150 && event.keyCode!=8)
	{
		event.returnValue = false;
		event.preventDefault();
	}
}
function textarea_length_feedback(event, val)
{
//    if(val.length==10)alert(val.length);
	if(val.length >= 600 && event.keyCode!=8)
	{
		event.returnValue = false;
		event.preventDefault();
	}
}

function set_edit_btn()
{
	$("input.edit").each(function(){
		$(this).click(function(){
			if($(this).val() == '修改')
			{
				$(this).val('保存');
				o = $(this).prev();
				c = o.clone().removeAttr('disabled');
				o.hide().after(c);
				c.focus();
			}
			else if($(this).val() == '保存')
			{
				$(this).val('修改');
				o = $(this).prev().prev();
				c = $(this).prev();
				o.val(c.val()).show();
				c.remove();
			}			
		});
	});
}
function login(){
	$('.error').html("");
	is_email_valid($('#email').val());
	if($.trim($('.error').html()) == "")
	{
		/*if($("#token-result").val() == 'r')
		{
			$("#login-form").submit();
		}
		else
		{
			alert("验证码有误");
            refresh_token();
		}*/
        $("#login-form").submit();
	}
}
function is_token_valid(str)
{
	/*token = $("#token").val();
	$.ajax({
		type:"get",
		dataType:"html",
		url:"/check_token/"+token,
		success:function(data){
			$("#token-result").val(data);
		}
	});*/
}
function refresh_token()
{
	$("#token-wrapper img").attr('src','/get_token/?r='+Math.random());
}
function enterToLogin(event)
{
	if(event.keyCode==13)
	{
		login();
	}
}
function enterToPass(event,obj1,obj2)
{
	if(event.keyCode==13)
	{
		obj1.blur();
        obj2.focus();
	}
}
function image_next()
{
	obj = $(".login-images .active");
	if(obj.attr('order') == "l")
	{
		$(".login-images img").first().addClass('active').fadeIn();
		obj.removeClass('active').fadeOut();
	}
	else
	{
		obj.removeClass("active").fadeOut();
		obj.next().addClass('active').fadeIn();
	}
}
function get_task_next_page(page,success,nomore,err){
    $('.pagination').html("加载中");
	page = parseInt(page)+1;
	$.ajax({
		url: '?type=ajax&page='+page,
		type: 'GET',
		dataType: 'html',
		timeout: 5000,
		error: function(){
			//alert('获取页面错误');
			$('.pagination').html("显示更多");
            if(err){
                err();
            }
		},
		success: function(data){
			if($.trim(data) == "")
			{
				$('.pagination').html("没有可显示的任务了");
                if(nomore){
                    nomore();
                }
				return;
			}            
			$('#pagination-page').val(page);
			$('.pagination').before(data);
			$('.pagination').html("显示更多");
            if(success){
                success();
            }
            if(_gaq){
                _gaq.push(['_trackPageview','tasks_more']);
            }
		}
	});
}
function ding(tid){
	$.ajax({
		url: '/task_ding/'+tid,
		type: 'GET',
		dataType: 'html',
		timeout: 5000,
		error: function(){
			alert('置顶成功!');
		},
		success: function(data){
			alert('置顶成功!');
		}
	});
}
$(document).ready(function(){

	//首先将#back-to-top隐藏

	$("#back-to-top").hide();

	//当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失

	$(function () {
		$(window).scroll(function(){
			if ($(window).scrollTop()>100){
				$("#back-to-top").fadeIn(1500);
			}
			else
			{
				$("#back-to-top").fadeOut(1500);
			}
		});

		//当点击跳转链接后，回到页面顶部位置

		$("#back-to-top").click(function(){
			$('body,html').animate({scrollTop:0},1000);
			return false;
		});
	});
});




