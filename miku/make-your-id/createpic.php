<?php
session_start();
$picname = $_SESSION["picture"];
$image =  'pict/'.$picname.'.jpg' ;
$db = mysql_select_db('articles_miku',mysql_connect('50.62.209.18:3306','articles_miku','e4Of87%k'));
$select3 = "SELECT * FROM `miku_id` WHERE `picture`='$image';";
$result3 = mysql_query($select3);
$row3 = mysql_fetch_array($result3);
$name = $row3['name'];

$useragent=$_SERVER['HTTP_USER_AGENT'];
if(preg_match('/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i',$useragent)||preg_match('/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i',substr($useragent,0,4)))
{
$file = "http://motherteresa.club/ncss/style_mm.css";
$logo = '<table width="100%"><tr><td width="20%"><a href=""><img src="http://motherteresa.club/npic/previous.png" width="90%"></a></center></td><td width="60%"><center><img src="http://funnymiku.in/logo_m.jpg" width="80%"></center></td><td width="20%"><a href=""><img src="http://motherteresa.club/npic/next.png" width="90%"></a></center></td></tr></table>';
$ads = '<center><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- mikuad1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:250px"
     data-ad-client="ca-pub-8558176112601390"
     data-ad-slot="2298854862"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></center>';
$data_width='280';
$fblike ='<br><br><div class="fb-page" data-href="https://www.facebook.com/funnymiku.in" data-width="280" data-hide-cover="false" data-show-facepile="true" data-show-posts="false"><div class="fb-xfbml-parse-ignore"><blockquote cite="https://www.facebook.com/funnymiku.in"><a href="https://www.facebook.com/funnymiku.in">Miku : The Funny Character</a></blockquote></div></div>';
}
else
{
$logo = '<img src="http://funnymiku.in/logo.jpg" height="100%">';
$file="http://motherteresa.club/ncss/style.css";
$ads = '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ads -->
<ins class="adsbygoogle"
     style="display:inline-block;width:980px;height:90px"
     data-ad-client="ca-pub-8558176112601390"
     data-ad-slot="7209083269"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>';
$data_width='580';
$fblike = '<br><br><div class="fb-page" data-href="https://www.facebook.com/funnymiku.in" data-width="580" data-hide-cover="false" data-show-facepile="true" data-show-posts="false"><div class="fb-xfbml-parse-ignore"><blockquote cite="https://www.facebook.com/funnymiku.in"><a href="https://www.facebook.com/funnymiku.in">Miku : The Funny Character</a></blockquote></div></div>
<div class="fb-comments" data-href="http://pics.motherteresa.club/'.$articleid.'.php" data-width="580" data-numposts="5" data-colorscheme="light"></div>';
}
?>
<html>
    <head>
<title>Create Your id</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="<?php echo $file; ?>">
<link rel="icon" type="image/png" href="http://articles.funnymiku.in/images/smily.png">
<meta name="title" content="<?php echo $name ;?> Has Created His Id"/>
<meta name="keywords" content="Funny Miku , FunnyMiku.in , Entertainment Videos , Funny Videos , Songs , Videos , Movies , <?php echo $title ; ?>">
<meta name="description" content="<?php echo $name ;?> Has Created His Own Id That Verified Him An Official Member Of The Group Miku Entertainment , Create Your Own"/>
<meta name="subject" content="Videos - FunnyMiku">
<meta name="copyright"content="FunnyMiku.in">
<meta name="revisit-after" content="10 seconds">
<meta name="og:title" content="<?php echo $name ;?> Has Created His Id"/>
<meta name="og:type" content="blog"/>
<meta name="og:image" content="http://funnymiku.in/make-your-id/<?php echo $image; ?>"/>
<meta name="og:site_name" content="FunnyMiku.in"/>
<meta name="og:description" content="<?php echo $name ;?> Has Created His Own Id That Verified Him An Official Member Of The Group Miku Entertainment , Create Your Own"/>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-59769228-1', 'auto');
  ga('send', 'pageview');

</script>
<style>


.btn {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
  background-image: -moz-linear-gradient(top, #3498db, #2980b9);
  background-image: -ms-linear-gradient(top, #3498db, #2980b9);
  background-image: -o-linear-gradient(top, #3498db, #2980b9);
  background-image: linear-gradient(to bottom, #3498db, #2980b9);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 28px;
  font-family: Arial;
  color: #ffffff;
  font-size: 20px;
  padding: 10px 20px 10px 20px;
  text-decoration: none;
}

.btn:hover {
  background: #3cb0fd;
  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);
  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);
  text-decoration: none;
}


</style>
<script>
document.getElementById('shareBtn').onclick = function() {
FB.ui(    {
  method: 'feed',
  picture: "http://funnymiku.in/make-your-id/<?php echo $image; ?>",
  description: "<?php echo $name ;?> Has Created His Own Id That Verified Him An Official Member Of The Group Miku Entertainment , Create Your Own here http://funnymiku.in/make-your-id/",
  
 }, function(response){});
}
</script>
    </head>
    <body onload="PostImage()">
        <div class="header">

               <center> <?php echo $logo; ?><br>
               </center>

        </div>
        <div id="container" class="rounded-10">
 <?php echo $ads; ?>
            <div class="left"><h1><?php echo $title; ?></h1>
                <div class="pic rounded-8" style="overflow:hidden;">
                     <br>
                    <center> 
<h1>Your Miku Id Is Been Sucessfully Creadted <a href="<?php echo $image; ?>">Download Image</a>
<br>
<br>
<input type="button" value="Share On Facebook" id ="shareBtn">
<br>
<br>

<div id="picture"><img src="<?php echo $image; ?>" width="95%"></div>
<br><br>

</center>

               </div>
            </div>
            <div class="right">
                <div class="pics rounded-10">
                 <div class="PopularPosts">
Most Recent<br>
                    </div>

 

                </div>
                <br><center>    
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- mikuad2 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-8558176112601390"
     data-ad-slot="8937694060"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</center>
<br><br>

            </div>
        </div>   

    </body>
       
</html>