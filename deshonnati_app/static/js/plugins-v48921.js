var config = {
    'min_width_req' : 200,
    'min_height_req': 200,
}

DE.plugins.link = {
    'name': 'Link',
    'label': 'Add Links',
    'color': '#3BB9FF',
    'requirelibs': [],
    'typedefs': {
        'type':[
            {'value':'dest', 'name':'Link to Page'},
            {'value':'uri', 'name':'External Link'},
            {'value':'call', 'name':'Mobile no.'},
            {'value':'email', 'name':'Email id'}
        ]
    },
    'attributes': {
        'id': '',
        'plugin':'',
        'type': 0,
        'value': '',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0
    },
    'onShow': function(item, pageKey){
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}

        //item has name and attributes
        //draw a box with attributes
        var link = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, 'a',pageKey);
        link.id = 'augment-box-'+item.attributes['id'];

        switch(item.attributes.type){
            case 'uri':
                //prepend http:// if not exists
                item.attributes.value = ( (item.attributes.value.indexOf('http://') == -1) && (item.attributes.value.indexOf('https://') == -1) )?
                    'http://'+item.attributes.value : item.attributes.value;
                link.setAttribute('target', '_blank');
                link.setAttribute('href', item.attributes.value);
            break;
            case 'dest':
                if(isNaN(Number(item.attributes.value))){
                    item.attributes.value = 1;
                }

                //if (typeof DE.changePageForSource === "function") {

                    link.setAttribute('href', 'javascript:;');
                    $(link).click(function(e) {
                        DE.changeHash('issue', item.attributes.value, 1);
                    });
                /*}else{

                    link.setAttribute('href', window.location.href.replace(window.location.hash, '')+
                        '#page/'+item.attributes.value+'/'+DE.zoom);
                }*/
            break;
            case 'call':
                
                link.setAttribute('target', '_blank');
                link.setAttribute('href', "tel:"+item.attributes.value);
            break;
            case 'email':
                
                link.setAttribute('target', '_blank');
                link.setAttribute('href', "mailto:"+item.attributes.value);
            break;
        }
        
            $(link).mousedown(function(e) {
                e.preventDefault();e.stopImmediatePropagation();
            });
            $(link).mouseup(function(e){
                e.preventDefault();e.stopImmediatePropagation();
            });
            $(link).click(function(e) {
                e.stopImmediatePropagation();
            });
        
                
        $('div[data-page-key="'+pageKey+'"]').append(link);
    },
    'isEditable': true,
    'onEdit': function(item){
        
    },
    'isEditable': function(attribute){
        switch(attribute){
            case 'type':
            case 'value':
                return true;
            break;
            default:
                return false;
        }
    }
};

DE.plugins.video = {
    'name': 'You Tube',
    'label': 'Add Video',
    'color': 'red',
    'requirelibs': [
        {'id':'swfobject', 'url':'full', 'src':'https://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js'},
        {'id':'iframe_api','url':'full','src':'https://www.youtube.com/iframe_api'}
    ],
    'typedefs':{},
    'attributes': {
        'id':'',
        'youtube-link':'',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0
    },
    'ytIdExtract':function(url)
        {
            var youtube_id;
            youtube_id = url.replace(/^[^v]+v.(.{11}).*/,"$1");
            if (/\bhttp:\/\//.test(youtube_id)){
                youtube_id = youtube_id.substr(youtube_id.length-11);
            }
            return youtube_id;
        },
    'playVideo': function(e){

        $(window).trigger('video_started');

        var ytId = $(e.currentTarget).attr('yt-id');
        var id = ytId;//$(e.currentTarget).attr('id');
        var width = parseInt(e.currentTarget.style.width);
        var height = parseInt(e.currentTarget.style.height);
        var params = {allowScriptAccess: "always"};
        var atts = {id: "ytapiplayer"};

        var html = '<div id="youtube-video-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">'+
                        '<div class="modal-dialog">'+
                            '<div class="modal-content">'+
                                '<div class="modal-header">'+
                                    '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>'+
                                    '<h4 class="modal-title" id="myModalLabel">Video</h4>'+
                                '</div>'+
                                '<div class="modal-body">'+
                                    '<div id="play-yt-'+id+'"></div></div>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+
                    '</div>';

        $(html).appendTo('body');

        $("#youtube-video-modal")
            .modal({
                'show':true,
                'backdrop':'static',
                'keyboard':false,
            })
            .on('hidden.bs.modal',function(){
                $(window).trigger('video_ended');
                $(this).remove();
            });

        // var params = { allowScriptAccess: 'always', allowFullScreen: 'true' };
        // swfobject.embedSWF("http://www.youtube.com/v/"+ytId+"?enablejsapi=1&playerapiid=ytplayer&autoplay=1", 'play-yt-'+id, "550", "350", "8", null, null, params);
        $("#play-yt-"+ytId).replaceWith('<div class="embed-container"><iframe src="//www.youtube.com/embed/'+ytId+'?autoplay=1" frameborder="0" allowfullscreen></iframe></div>');

        e.preventDefault();e.stopImmediatePropagation();
    },
    'onShow': function(item, pageKey, mode='page'){
        if (item.attributes['youtube-link']=='') return;
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}

        //show youtube video
        var video = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        video.id = 'augment-box-'+item.attributes['id'];
        
        var width = $(video).width();
        var height = $(video).height();

        var ytId = this.ytIdExtract(item.attributes['youtube-link']);
        var show_link = true;

        var play_btn = document.createElement('div');
        play_btn.setAttribute('data-plugin-id',item.attributes['id']);
        play_btn.setAttribute('yt-id', ytId);
        play_btn.setAttribute('class','de-play-icon');
        video.appendChild(play_btn);

        var logo = document.createElement('div');
        logo.setAttribute('data-plugin-id',item.attributes['id']);
        logo.setAttribute('class','de-logo');

        var play_link = document.createElement('div');
        play_link.setAttribute('class', 'de-link-to-play');
        play_link.setAttribute('data-plugin-id',item.attributes['id']);
        play_link.setAttribute('yt-id', ytId);
        play_link.setAttribute('id', 'ytapiplayer_'+ytId);
                
        var html = '<a> Video </a>';
        $(play_link).append(html);
        $(play_link).append(logo);

        var thisObj = this;

        $(video).mouseup(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).mousedown(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).hover(function(e) {
            if(show_link) {
                video.appendChild(play_link);
                show_link = false;
            } else {
                video.removeChild(play_link);
                show_link = true;
            }
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        });
        $(play_link).click(this.playVideo);
        $(play_btn).click(this.playVideo);
        $('div[data-page-key="'+pageKey+'"]').append(video);
        if( mode == 'clip'){

            $("#de-chunks-container").append(video);
        }
    },
    'onShowV2': function(item, pageKey){

        $('div[data-page-key]').not('div[data-page-key="'+pageKey+'"]').find('.augmented-box').remove();

        //show youtube video
        var video = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        
        video.setAttribute('id', "yt-video-"+item.attributes['id']);

        var width = $(video).width();
        var height = $(video).height();

        if( width < config.min_width_req && height < config.min_height_req ){

            $('#augment-box-'+item.attributes['id']).remove();
            this.onShow(item, pageKey);
            return;
        }    

        if( typeof(YT) == 'undefined' || typeof(YT.Player) == 'undefined' ){
            setTimeout(function(){
                this.onShowV2(item, pageKey)
            }.bind(this), 100);
            return;
        }


        var ytId = this.ytIdExtract(item.attributes['youtube-link']);

        var html = '<iframe id='+ytId+' class="youtube-player" type="text/html" width="'+width+'" height="'+height+'" allowfullscreen="1"  src="https://www.youtube.com/embed/'+ytId+'?enablejsapi=1&origin='+window.location.origin+'" autoplay="1" frameborder="0" ></iframe>';

        video.insertAdjacentHTML( 'beforeend', html );
        //$("#yt-video-video-box-1566887177996").html(html);
       /* var video_thumbnail = document.createElement('img');
        video_thumbnail.setAttribute('src','//img.youtube.com/vi/'+ytId+'/0.jpg');
        video_thumbnail.setAttribute('width',width);
        video_thumbnail.setAttribute('height',height);
        
        video.appendChild(video_thumbnail);

        var play_btn = document.createElement('div');
        play_btn.setAttribute('data-plugin-id',item.attributes['id']);
        play_btn.setAttribute('yt-id', ytId);
        play_btn.setAttribute('class','de-play-icon');
        video.appendChild(play_btn);*/

        $('div[data-page-key="'+pageKey+'"]').append(video);


        player = new YT.Player(ytId, {
            videoId: ytId,
            events: {
                'onReady': this.onPlayerReady,
                'onStateChange': this.onPlayerStateChange
            }
        })    
        //$(play_btn).click(this.playVideoV2);

    },
    'onPlayerReady': function(event) {
        event.target.playVideo();
    },
    'onPlayerStateChange': function(event) {
        if (event.data == YT.PlayerState.PLAYING) {
            $(window).trigger('video_started');
        }else{
            $(window).trigger('video_ended');
        }
    },
    'playVideoV2': function(e){
        // not in use
        $(window).trigger('video_started');
        var ytId = $(e.currentTarget).attr('yt-id');
        var id = $(e.currentTarget.parentElement).attr('id');
        var width = parseInt(e.currentTarget.parentElement.style.width);
        var height = parseInt(e.currentTarget.parentElement.style.height);
        var params = {allowScriptAccess: "always"};
        var atts = {id: "ytapiplayer"};
        
        var html = '<iframe id='+ytId+' class="youtube-player" type="text/html" width="'+width+'" height="'+height+'" allowfullscreen="1" allow="autoplay" src="https://www.youtube.com/embed/'+ytId+'?autoplay=1" frameborder="0" ></iframe>';

        $("#"+id).html(html);

       /* var html = "<div id="+ytId+"></div>";

        $("#"+id).html(html);
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);*/

       /* var vid = document.getElementById(ytId);
        vid.onStateChange = function() {
            alert("ENDED");
            $(window).trigger('video_ended');
        };
        vid.play = function() {
            alert("play");
            //$(window).trigger('video_ended');
        };*/
        e.preventDefault();e.stopImmediatePropagation();

    },
    'onEdit': function(item){
        
    },
    'isEditable': function(attribute){
        switch(attribute){
        case 'youtube-link':
            return true;
        default:
            return false;
        }
    }
};

DE.plugins.form = {
    'name': 'Form',
    'label': 'Add Form',
    'color': '#EBAFFF',
    'requirelibs': [],
    'typedefs':{
        'field-type-1':[
            {'value':'Text', 'name':'Text'},
            {'value':'Paragraph', 'name':'Paragraph'},
            {'value':'Checkbox', 'name':'Checkbox'},
        ],
        'field-type-2':[
            {'value':'Text', 'name':'Text'},
            {'value':'Paragraph', 'name':'Paragraph'},
            {'value':'Checkbox', 'name':'Checkbox'},
        ],
        'field-type-3':[
            {'value':'Text', 'name':'Text'},
            {'value':'Paragraph', 'name':'Paragraph'},
            {'value':'Checkbox', 'name':'Checkbox'},
        ],
        'field-type-4':[
            {'value':'Text', 'name':'Text'},
            {'value':'Paragraph', 'name':'Paragraph'},
            {'value':'Checkbox', 'name':'Checkbox'},
        ],
        'field-type-5':[
            {'value':'Text', 'name':'Text'},
            {'value':'Paragraph', 'name':'Paragraph'},
            {'value':'Checkbox', 'name':'Checkbox'},
        ]
    },
    'attributes': {
        'id':'',
        'form-title':'',
        'field-1':'',
        'field-type-1':'',
        'field-2':'',
        'field-type-2':'',
        'field-3':'',
        'field-type-3':'',
        'field-4':'',
        'field-type-4':'',
        'field-5':'',
        'field-type-5':'',
        'mail-at':'',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0
    },
    'buttons':[
     {"name":"form submission",
      "callback":function(){
           var form_box_id = $("#form_box_id").html();    
            if (form_box_id.search(/^form-/i)!=-1){

                OpenWindow=window.open("", "newwin","width=800, height=500, location=0");
                $.getJSON(DE.viewer_url+'attributes/getformdata/'+form_box_id+"?callback=?", function(json_object){
                    //json_object = JSON.parse(json_data);
                    var window_html = '<table width="100%" border="1">';
                    window_html +=  '<tr>'+
                                    '<td>SN</td>'+
                                    '<td>'+$("[name='field-1']").val()+'</td>'+
                                    '<td>'+$("[name='field-2']").val()+'</td>'+
                                    '<td>'+$("[name='field-3']").val()+'</td>'+
                                    '<td>'+$("[name='field-4']").val()+'</td>'+
                                    '<td>'+$("[name='field-5']").val()+'</td>'+
                                    '</tr>';

                    for (i=0 ; i< json_object.length; i++){
                        window_html += '<tr>';
                        window_html += '<td>' + (i+1) + '</td>';
                        window_html += '<td>' + json_object[i].attributes['field-1'] + '</td>';
                        window_html += '<td>' + json_object[i].attributes['field-2'] + '</td>';
                        window_html += '<td>' + json_object[i].attributes['field-3'] + '</td>';
                        window_html += '<td>' + json_object[i].attributes['field-4'] + '</td>';
                        window_html += '<td>' + json_object[i].attributes['field-5'] + '</td>';
                        window_html += '</tr>';
                    }
                    window_html += '</table>';
                    OpenWindow.document.write(window_html);
                });

            }  
     }}
    ],
    'isEditable': function(attribute){
        switch(attribute){
        case 'form-title':
        case 'field-type-1':
        case 'field-1':
        case 'field-type-2':
        case 'field-2':
        case 'field-type-3':
        case 'field-3':
        case 'field-type-4':
        case 'field-4':
        case 'field-type-5':
        case 'field-5':
        case 'mail-at':
            return true;
        default:
            return false;
        }
    },
    'onShow': function(item, pageKey){
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}

        //show youtube video
        var form_btn = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        form_btn.id = 'augment-box-'+item.attributes['id'];

        var show_link = true;

        var form_icon = document.createElement('div');
        form_icon.setAttribute('data-plugin-id',item.attributes['id']);
        form_icon.setAttribute('class','de-form-icon');
        form_btn.appendChild(form_icon);

        var logo = document.createElement('div');
        logo.setAttribute('data-plugin-id',item.attributes['id']);
        logo.setAttribute('class','de-logo');
        
        var open_link = document.createElement('div');
        open_link.setAttribute('class', 'de-link-to-play');

        var html = '<a> Form </a>';
        $(open_link).append(html);
        $(open_link).append(logo);

        $(form_btn)
            .mouseup(function(e){
                e.preventDefault();e.stopImmediatePropagation();
            }).mousedown(function(e){
                e.preventDefault();e.stopImmediatePropagation();
            }).hover(function(e) {
                if(show_link) {
                    form_btn.appendChild(open_link);
                    show_link = false;
                } else {
                    form_btn.removeChild(open_link);
                    show_link = true;
                }
                e.preventDefault();e.stopImmediatePropagation();
            }).click(function(e) {
                e.preventDefault();e.stopImmediatePropagation();
            });

            var trans_layer = $(open_link);
            var icon = $(form_icon);
            var combined = trans_layer.add(icon)

            $(combined).click(function(e){
               e.stopImmediatePropagation();
               var form_html='';
                
                $('<div id="form-box"></div>').appendTo('body');
                
                form_html += '<form id="plugin_form" method="POST" action="'+DE.baseUrl+'attributes/submitform/'+item.attributes.pagekey+'/'+item.attributes.id+'">';
                form_html += '<table width="100%">';
                form_html += '<tr><td><div id="plugin_form_thank_you_div"></div></td></tr>';
                form_html += '<tr><td><input type="hidden" name="form-id" value="'+item.attributes['id']+'" /></td></tr>';
                form_html += '<tr><td><input type="hidden" name="redire-to" value="'+window.location.href+'" /></td></tr>';
                    
                for (i=1;i<=5;i++){
                    
                    if (item.attributes['field-'+i]){
                        
                        form_html += '<tr>';
                        
                        var element_type = item.attributes['field-type-'+i];
                        
                        
                        form_html += '<td style="vertical-align: middle;">'+item.attributes['field-'+i]+'</td><td>';
                        
                        if (element_type=='Text'){
                            form_html += '<input type="text" size="30" name="field-'+i+'" />';
                        }
                        if (element_type=='Paragraph'){
                            form_html += '<textarea rows="4" cols="30" name="field-'+i+'"></textarea>';
                        }
                        if (element_type=='Checkbox'){
                            form_html += '<input type="checkbox" name="field-'+i+'" value="'+item.attributes['field-'+i]+'" />';
                        }

                        form_html += '</td></tr>';
                    }
                }
                
                form_html += '<tr><td colspan="2"><input type="button" value="Submit" name="submit" id="submit" /></td></tr>';
                form_html += '</form>';
                
                form_html +=    '<script type="text/javascript">'+
                                    '$("#submit").click(function(){'+
                                        'form_data=$("#plugin_form").serialize();'+ 
                                        '$.ajax({'+
                                            'type:"POST",'+ 
                                            'data:form_data,'+
                                            'url:"'+DEConfig.baseUrl+'attributes/submitform/'+item.attributes.pagekey+'/'+item.attributes.id+'",'+
                                            'success:function(){'+
                                                '$("#form-box").html("<div style=\'width:100%; height:100px; text-align:center; vertical-align:middle;\'><br>Your information has been submitted.<br><br><input type=\'button\' value=\'Close\' onclick=$(\'#form-box\').remove() /></div>");'+
                                            '}'+
                                        '});'+
                                    '});'+
                                '</script>';
                
                $('#form-box').html(form_html);
                
               $('#form-box').dialog({'center':true,
                    'autoOpen':true,
                    'width':445,
                    'title':item.attributes['form-title'],
                    'close':function(){$('#form-box').remove()}}
                ).show();
                
                   
            });
            
        $('div[data-page-key="'+pageKey+'"]').append(form_btn);
    },
    'showForm': function(){
        
    },
    'onEdit': function(item){
        
    }
};

DE.plugins.poll = {
    'name': 'Poll',
    'label': 'Add Poll Widgets',
    'color': 'orange',
    'requirelibs': [],
    'isEditable': true,
    'attributes': {
        'id': '',
        'plugin':'',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0,
        'poll-daddy-embed-code':''
    },
    'typedefs': {
        'poll-daddy-embed-code':'multiline'
    },
    'onShow': function(item, pageKey){
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}

        //show slide share 
        var poll = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        poll.id = 'augment-box-'+item.attributes['id'];

        var frame = '<iframe id="frame-'+item.attributes['id']+'" width='+parseInt(poll.style.width)+' height='+parseInt(poll.style.height)+' marginheight="0" marginwidth="0" frameborder="0"></iframe>';
        $(frame).appendTo(poll);
        $(poll).mouseup(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).mousedown(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        });
        $("#de-chunks-container").append(poll);
        
        if (item.attributes['poll-daddy-embed-code'].indexOf('polldaddy.com/')!=-1){
            var ifrm = document.getElementById("frame-"+item.attributes['id']);
            if (ifrm){
                ifrm = (ifrm.contentWindow) ? ifrm.contentWindow : (ifrm.contentDocument.document) ? ifrm.contentDocument.document : ifrm.contentDocument;
                ifrm.document.open();
                ifrm.document.write(item.attributes['poll-daddy-embed-code']);
                ifrm.document.close();
            }
        }
    },
    'onEdit': function(item){
        
    },
    'isEditable': function(attribute){
        switch(attribute){
            case 'poll-daddy-embed-code':
                return true;
            break;
            default:
                return false;
        }
    }
}

DE.plugins.upload_video = {
    'name': 'Video',
    'label': 'Add video',
    'color': 'lightyellow',
    'requirelibs': [
                        {'id':'flowplayer', 'url':'full', 'src':'https://releases.flowplayer.org/js/flowplayer-3.2.11.min.js'}
                    ],
    'isEditable': true,
    'attributes': {
        'id': '',
        'plugin':'',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0
    },
    'playvideo': function(e){

        $(window).trigger('video_started');
        var video_url = $(e.currentTarget).attr('video_url');
        var elem_id = 'play-uv-'+$(e.currentTarget).attr('data-plugin-id');

        var is_html5_video = (typeof(document.createElement('video').canPlayType) != 'undefined') ? true : false;
        if( is_html5_video ){


            var html = '<div><video autoplay width="305" height="310" controls><source src ="'+video_url.replace('http:','https:')+'" id="'+elem_id+'" type="video/mp4"></div>';
            $(html).dialog({
                'title':'Related Video',
                'width':'350',
                'height':'350',
                'modal':true,
                'resizable':false,
                'draggable': false,
                'close':function(){
                    $(window).trigger('video_ended');
                    $(this).remove();
                }
            });
        }else{

             var html = '<div><a href="'+video_url.replace('http:','https:')+'" id="'+elem_id+'"></a></div>';
            $(html).dialog({
                'title':'Related Video',
                'width':'400',
                'height':'400',
                'modal':true,
                'resizable':false,
                'draggable': false,
                'close':function(){
                    $(window).trigger('video_ended');
                    $(this).remove();
                }
            });
            $f(elem_id, "https://releases.flowplayer.org/swf/flowplayer-3.2.12.swf", {});
        }
    },
    'playvideoV2': function(e){

        //$(window).trigger('video_started');
        var video_url = $(e.currentTarget).attr('video_url');
        var item_id = $(e.currentTarget).attr('data-plugin-id');
        var elem_id = 'play-uv-'+item_id;

        var width = $("#augment-box-"+item_id).width();
        var height = $("#augment-box-"+item_id).height();

        var is_html5_video = (typeof(document.createElement('video').canPlayType) != 'undefined') ? true : false;
        var html ='';
        if( is_html5_video ){

            html = '<div style="background: black;"><video id="upload_video-'+item_id+'" autoplay width="'+width+'" height="'+height+'" controls><source src ="'+video_url.replace('http:','https:')+'" id="'+elem_id+'" type="video/mp4"></div>';
        }else{

            html = '<div><a href="'+video_url.replace('http:','https:')+'" id="'+elem_id+'"></a></div>';
            $f(elem_id, "https://releases.flowplayer.org/swf/flowplayer-3.2.18.swf", {});
        }

        $('#augment-box-'+item_id).html(html);

        var vid = document.getElementById("upload_video-"+item_id);
        vid.onended = function() {
            $(window).trigger('video_ended');
        };
        vid.onpause = function() {
            $(window).trigger('video_ended');
        };
        vid.onplay = function() {
            $(window).trigger('video_started');
        };
    },
    'onShow': function(item, pageKey,mode='page'){
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}
        
        var video = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        video.id = 'augment-box-'+item.attributes['id'];

        var width = $(video).width();
        var height = $(video).height();

        var show_link = true;

        var play_btn = document.createElement('div');
        play_btn.setAttribute('data-plugin-id',item.attributes['id']);
        play_btn.setAttribute('class','de-play-icon');
        play_btn.setAttribute('video_url',item.attributes['video_url']);
        video.appendChild(play_btn);

        var logo = document.createElement('div');
        logo.setAttribute('data-plugin-id',item.attributes['id']);
        logo.setAttribute('class','de-logo');

        var play_link = document.createElement('div');
        play_link.setAttribute('class', 'de-link-to-play');
        play_link.setAttribute('data-plugin-id',item.attributes['id']);
        play_link.setAttribute('video_url',item.attributes['video_url']);
        
        var html = '<a> Video </a>';
        $(play_link).append(html);
        $(play_link).append(logo);

        $(video).mouseup(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).mousedown(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).hover(function(e) {
            if(show_link) {
                video.appendChild(play_link);
                show_link = false;
            } else {
                video.removeChild(play_link);
                show_link = true;
            }
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        });

        
        $('div[data-page-key="'+pageKey+'"]').append(video);

        $(play_link).click(this.playvideo);
        $(play_btn).click(this.playvideo);
        if( mode == 'clip'){

            $("#de-chunks-container").append(video);
        }
    },
    'onShowV2': function(item, pageKey){
        if (document.getElementById('augment-box-'+item.attributes['id'])){return;}
        
        var video = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        video.id = 'augment-box-'+item.attributes['id'];

        var width = $(video).width();
        var height = $(video).height();
        
        if( width < config.min_width_req && height < config.min_height_req ){

            $('#augment-box-'+item.attributes['id']).remove();
            this.onShow(item, pageKey);
            return;
        }

        var show_link = true;

        var play_btn = document.createElement('div');
        play_btn.setAttribute('data-plugin-id',item.attributes['id']);
        play_btn.setAttribute('class','de-play-icon');
        play_btn.setAttribute('video_url',item.attributes['video_url']);
        video.appendChild(play_btn);

        var logo = document.createElement('div');
        logo.setAttribute('data-plugin-id',item.attributes['id']);
        logo.setAttribute('class','de-logo');

        var play_link = document.createElement('div');
        play_link.setAttribute('class', 'de-link-to-play');
        play_link.setAttribute('data-plugin-id',item.attributes['id']);
        play_link.setAttribute('video_url',item.attributes['video_url']);
        
        var html = '<a> Video </a>';
        $(play_link).append(html);
        $(play_link).append(logo);

        $(video).mouseup(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).mousedown(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).hover(function(e) {
            if(show_link) {
                video.appendChild(play_link);
                show_link = false;
            } else {
                video.removeChild(play_link);
                show_link = true;
            }
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        });

        
        $('div[data-page-key="'+pageKey+'"]').append(video);

        $(play_link).click(this.playvideoV2);
        $(play_btn).click(this.playvideoV2);
        
    },    
    'onEdit': function(item){
        
    },
    'isEditable': function(attribute){
        switch(attribute){
            default:
                return false;
        }
    }
}

DE.plugins.gallery = {
    'name': 'Gallery',
    'label': 'Add Image Gallery',
    'color': '#4CC417',
    'isEditable': true,
    'requirelibs': [
        /*{'id':'bxsliderjs', 'url': 'partial','src':'design-elements/bx-slider/jquery.bxslider.min.js'},
        {'id':'bxslidercss', 'url': 'partial', 'src':'design-elements/bx-slider/jquery.bxslider.css'},*/
        {'id':'responsiveslidecss', 'url': 'partial', 'src':'/design-elements/ResponsiveSlides.js-master/responsiveslides.css'},
        {'id':'responsiveslidejs', 'url': 'partial','src':'/design-elements/ResponsiveSlides.js-master/responsiveslides.js'},
        {'id':'slickslidecss', 'url': 'partial', 'src':'/design-elements/slick-1.8/slick/slick.css'},
        {'id':'slickslidejs', 'url': 'partial','src':'/design-elements/slick-1.8/slick/slick.js'},
        {'id':'slickslidethemecss', 'url': 'partial','src':'/design-elements/slick-1.8/slick/slick-theme.css'}
    ],
    'typedefs': {
        'upload-files':'file'
    },

    'isEditable': true,
    'attributes': {
        'id': '',
        'plugin':'',
        'images': '',
        'x0':0,
        'x1':0,
        'y0':0,
        'y1':0
    },
    'createGallery': function(e) {
        var id = $(e.currentTarget).attr('data-plugin-id') ? $(e.currentTarget).attr('data-plugin-id') : e.attributes['id'] ;
        var ui = $("#"+id);
        /*if (ui.length<1){
            setTimeout(function(){
                DE.plugins.gallery.createGallery(e);
            },500);
        }else{
            var slider = ui.bxSlider();
        }*/
        /*if (typeof $.fn.bxSlider != 'undefined') { 

            $('#'+id).bxSlider();
        
        } else {

            setTimeout(function(){
                DE.plugins.gallery.createGallery(e);
            },500);
        }*/
        if (ui.length<1){
            
            setTimeout(function(){
                DE.plugins.gallery.createGallery(e);
            },500);
        }else{

            $('#'+id).responsiveSlides({
                    nav: true,
                    pager: true,
                });
        }
        /*if (typeof $.fn.responsiveSlides != 'undefined') {
            
            $('#'+id).responsiveSlides({
                auto: false,
                nav: true,
                pager: true
            });
        
        } else {
            setTimeout(function(){
                DE.plugins.gallery.createGallery(e);
            },500);
        }*/
    },
    'slideshow': function(e){  
        //if( e.preventDefault != null ){

            //e.preventDefault();e.stopImmediatePropagation();
        //}
        var id = $(e.currentTarget).attr('data-plugin-id') ? $(e.currentTarget).attr('data-plugin-id') : e.attributes['id'] ;
        var images = $(e.currentTarget).attr('data-images') ? $(e.currentTarget).attr('data-images') : e.attributes['images'];
        var width = $(e.currentTarget).attr('data-image-width');
        var height = $(e.currentTarget).attr('data-image-height');
        
        var img_src = new Array();
        img_src = Array.isArray(images)? images : images.split(",");

        var html = '<div id="gallery-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">'+
                        '<div class="modal-dialog">'+
                            '<div class="modal-content">'+
                                '<div class="modal-header">'+
                                    '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>'+
                                    '<h4 class="modal-title" id="myModalLabel">Gallery</h4>'+
                                '</div>'+
                                '<div class="modal-body">'+
                                '</div>'+
                            '</div>'+
                        '</div>'+
                    '</div>';

        $(html).appendTo('body');

        $("#gallery-modal")
            .modal({
                'show':true,
                'backdrop':'static',
                'keyboard':false,
            })
            .on('hidden.bs.modal',function(){
                
                $(this).remove();
            });
            /*.on('show', function () {
               $(this).find('.modal-body').css({
                      width:'auto', //probably not needed
                      height:'auto', //probably not needed 
                      'max-height':'100%'
               })
            });*/

        html = '<ul id="'+id+'">';
        for (var idx in img_src) {
            html += '<li style="text-align:center;"><img src="'+img_src[idx].replace('http:','https:')+'" width=460 height=380></li>';
        }
        html += '</ul>';
        $("#gallery-modal .modal-body").append(html);

        DE.plugins.gallery.createGallery(e);
    },
    'onShow': function(item, pageKey,mode='page'){
        if (document.getElementById('augment-box-'+item.attributes['id'])){
            return;
        }
        //item has name and attributes
        //draw a box with attributes
        var gallery = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);
        gallery.id = 'augment-box-'+item.attributes['id'];
        gallery.setAttribute('data-plugin-id',item.attributes['id']);

        var width = $(gallery).width();
        var height = $(gallery).height();

        var show_link = true;

        var gallery_btn = document.createElement('div');
        gallery_btn.setAttribute('data-plugin-id',item.attributes['id']);
        gallery_btn.setAttribute('data-images',item.attributes['images']);
        gallery_btn.setAttribute('data-image-width',width);
        gallery_btn.setAttribute('data-image-height',height);
        gallery_btn.setAttribute('class','de-gallery-icon');
        gallery.appendChild(gallery_btn);

        var logo = document.createElement('div');
        logo.setAttribute('data-plugin-id',item.attributes['id']);
        logo.setAttribute('class','de-logo');
        
        var play_link = document.createElement('div');
        play_link.setAttribute('class', 'de-link-to-play');
        play_link.setAttribute('data-plugin-id',item.attributes['id']);
        play_link.setAttribute('data-images',item.attributes['images']);
        play_link.setAttribute('data-image-width',width);
        play_link.setAttribute('data-image-height',height);
        
        var html = '<a> Gallery </a>';
        $(play_link).append(html);
        $(play_link).append(logo);

        $(gallery).mouseup(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).mousedown(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        }).hover(function(e) {
            if(show_link) {
                gallery.appendChild(play_link);
                show_link = false;
            } else {
                gallery.removeChild(play_link);
                show_link = true;
            }
            e.preventDefault();e.stopImmediatePropagation();
        }).click(function(e){
            e.preventDefault();e.stopImmediatePropagation();
        });

        $('div[data-page-key="'+pageKey+'"]').append(gallery);
        
        $(play_link).click(this.slideshow);
        $(gallery_btn).click(this.slideshow);
        if( mode == 'clip'){

            $("#de-chunks-container").append(gallery);
        }
    },
    'slideshowV2': function(e) {

        if (typeof $.fn.slick != 'undefined') {
            
            var currThis = this;

            $("#augmented-box-"+e.attributes['id']).show();

            $('#'+e.attributes['id']+'_ul').slick({
                autoplay: true,
                mobileFirst: true,
                arrows: false,
            });

            

           /* $('#'+e.attributes['id']+'_ul').on('beforeChange', function(event, slick, currentSlide, nextSlide){*/
            $("#"+e.attributes['id']+"_ul li img").click(function(event){
                event.preventDefault();event.stopImmediatePropagation();
                currThis.slideshow(e);
            });
            /*});*/

           /* $('#'+e.attributes['id']+'_ul').on('init', function(slick){

              console.log("ersadfasdfas");
            });*/
            /*$('#'+e.attributes['id']+'_ul').responsiveSlides({
                
                before: function(){

                    console.log("dsafasd");
                    $("#"+e.attributes['id']+"_ul li img").click(function(event){
                        event.preventDefault();event.stopImmediatePropagation();
                        currThis.slideshow(e);
                    });
                }
            }); */  
        
        } else {
            /*slideshowV2 = this.slideshowV2;
            setTimeout(function(){slideshowV2(e);}, 100);*/
             setTimeout(function(){
                this.slideshowV2(e);
            }.bind(this), 100);

        }
    },
    'onShowV2': function(item, pageKey) {
        //item has name and attributes
        //draw a box with attributes

        var gallery = DE.drawAugmentedBox(item.attributes.x0, item.attributes.y0,
            item.attributes.x1, item.attributes.y1, "" , pageKey);

        gallery.setAttribute('id', "augmented-box-"+item.attributes['id']);
        var width = $(gallery).width();
        var height = $(gallery).height();

        /*if( width < config.min_width_req && height < config.min_height_req ){

            $('#augment-box-'+item.attributes['id']).remove();
            this.onShow(item, pageKey);
            return;
        }*/

        var img_slider = document.createElement("ul");
        
        img_slider.setAttribute('id',item.attributes['id']+'_ul');

        for (var i = 0; i < item.attributes['images'].length; i++) {
            
            var li = document.createElement("li");

            var img_html = document.createElement('img');
            img_html.setAttribute('src', item.attributes['images'][i]);
            img_html.setAttribute('width',width);
            img_html.setAttribute('height',height);

            li.appendChild(img_html);
            img_slider.appendChild(li);
        }
        
        gallery.appendChild(img_slider);

        $('div[data-page-key="'+pageKey+'"]').append(gallery);
        document.getElementById('augmented-box-'+item.attributes['id']).style.display = 'none';
        this.slideshowV2(item);
    },
    'onEdit': function(item){
        
    },
    'isEditable': function(attribute){
        switch(attribute){
            case 'upload-files':
                return true;
            break;
            default:
                return false;
        }
    }
}