<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
        <title>Agroxa - Responsive Bootstrap 4 Admin Dashboard</title>
        <meta content="Admin Dashboard" name="description" />
        <meta content="Themesbrand" name="author" />
        <link rel="shortcut icon" href="../images/favicon.ico">

        <link rel="stylesheet" href="../../../plugins/morris/morris.css">

        <link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css">
        <link href="../css/metismenu.min.css" rel="stylesheet" type="text/css">
        <link href="../css/icons.css" rel="stylesheet" type="text/css">
        <link href="../css/style.css" rel="stylesheet" type="text/css">
    </head>

    <body>

        <!-- Begin page -->
        <div id="wrapper">

            <!-- Top Bar Start -->
            <div class="topbar">

                <!-- LOGO -->
                <div class="topbar-left">
                    <a href="index.html" class="logo">
                        <span>
                            <img src="assets/images/logo.png" alt="" height="24">
                        </span>
                        <i>
                            <img src="assets/images/logo-sm.png" alt="" height="22">
                        </i>
                    </a>
                </div>

                <nav class="navbar-custom">

                    <ul class="navbar-right d-flex list-inline float-right mb-0">
                        <li class="dropdown notification-list d-none d-sm-block">
                            <form role="search" class="app-search">
                                <div class="form-group mb-0"> 
                                    <input type="text" class="form-control" placeholder="Search..">
                                    <button type="submit"><i class="fa fa-search"></i></button>
                                </div>
                            </form> 
                        </li>

                        <li class="dropdown notification-list">
                            <a class="nav-link dropdown-toggle arrow-none waves-effect waves-light" data-toggle="dropdown" href="#" role="button" aria-haspopup="false" aria-expanded="false">
                                <i class="mdi mdi-bell noti-icon"></i>
                                <span class="badge badge-pill badge-info noti-icon-badge">3</span>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right dropdown-menu-lg">
                                <!-- item-->
                                <h6 class="dropdown-item-text">
                                    Notifications
                                </h6>
                                <!-- All-->
                                <a href="javascript:void(0);" class="dropdown-item text-center text-primary">
                                    View all <i class="fi-arrow-right"></i>
                                </a>
                            </div>        
                        </li>
                        <li class="dropdown notification-list">
                            <div class="dropdown notification-list nav-pro-img">
                                <a class="dropdown-toggle nav-link arrow-none waves-effect nav-user waves-light" data-toggle="dropdown" href="#" role="button" aria-haspopup="false" aria-expanded="false">
                                    <img src="assets/images/users/user-4.jpg" alt="user" class="rounded-circle">
                                </a>                                                                   
                            </div>
                        </li>

                    </ul>

                    <ul class="list-inline menu-left mb-0">
                        <li class="float-left">
                            <button class="button-menu-mobile open-left waves-effect waves-light">
                                <i class="mdi mdi-menu"></i>
                            </button>
                        </li>                        
                    </ul>

                </nav>

            </div>
            <!-- Top Bar End -->

			
            <!-- ========== Left Sidebar Start ========== -->
            <div class="left side-menu">
                <div class="slimscroll-menu" id="remove-scroll">

                    <!--- Sidemenu -->
                    <div id="sidebar-menu">
                        <!-- Left Menu Start -->
                        <ul class="metismenu" id="side-menu">
                            <li class="menu-title">Main</li>
                            <li>
                                <a href="index.html" class="waves-effect">
                                    <i class="mdi mdi-home"></i><span class="badge badge-primary float-right">3</span> <span> Dashboard </span>
                                </a>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-email"></i><span> Email <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span></a>
                                <ul class="submenu">
                                    <li><a href="email-inbox.html">Inbox</a></li>
                                    <li><a href="email-read.html">Email Read</a></li>
                                    <li><a href="email-compose.html">Email Compose</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-buffer"></i> <span> UI Elements <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span> </a>
                                <ul class="submenu">
                                    <li><a href="ui-alerts.html">Alerts</a></li>
                                    <li><a href="ui-buttons.html">Buttons</a></li>
                                    <li><a href="ui-badge.html">Badge</a></li>
                                    <li><a href="ui-cards.html">Cards</a></li>
                                    <li><a href="ui-carousel.html">Carousel</a></li>
                                    <li><a href="ui-dropdowns.html">Dropdowns</a></li>
                                    <li><a href="ui-grid.html">Grid</a></li>
                                    <li><a href="ui-images.html">Images</a></li>
                                    <li><a href="ui-modals.html">Modals</a></li>
                                    <li><a href="ui-pagination.html">Pagination</a></li>
                                    <li><a href="ui-popover-tooltips.html">Popover & Tooltips</a></li>
                                    <li><a href="ui-progressbars.html">Progress Bars</a></li>
                                    <li><a href="ui-tabs-accordions.html">Tabs & Accordions</a></li>
                                    <li><a href="ui-typography.html">Typography</a></li>
                                    <li><a href="ui-video.html">Video</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-black-mesa"></i> <span> Components <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span> </a>
                                <ul class="submenu">
                                    <li><a href="components-lightbox.html">Lightbox</a></li>
                                    <li><a href="components-rangeslider.html">Range Slider</a></li>
                                    <li><a href="components-session-timeout.html">Session Timeout</a></li>
                                    <li><a href="components-sweet-alert.html">Sweet-Alert</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-clipboard"></i><span> Forms <span class="badge badge-success float-right">6</span> </span></a>
                                <ul class="submenu">
                                    <li><a href="form-elements.html">Form Elements</a></li>
                                    <li><a href="form-validation.html">Form Validation</a></li>
                                    <li><a href="form-advanced.html">Form Advanced</a></li>
                                    <li><a href="form-editors.html">Form Editors</a></li>
                                    <li><a href="form-uploads.html">Form File Upload</a></li>
                                    <li><a href="form-xeditable.html">Form Xeditable</a></li>

                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-finance"></i><span> Charts <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span></a>
                                <ul class="submenu">
                                    <li><a href="charts-chartist.html">Chartist Chart</a></li>
                                    <li><a href="charts-chartjs.html">Chartjs Chart</a></li>
                                    <li><a href="charts-flot.html">Flot Chart</a></li>
                                    <li><a href="charts-c3.html">C3 Chart</a></li>
                                    <li><a href="charts-morris.html">Morris Chart</a></li>
                                    <li><a href="charts-other.html">Jquery Knob Chart</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-table-settings"></i><span> Tables <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span></a>
                                <ul class="submenu">
                                    <li><a href="tables-basic.html">Basic Tables</a></li>
                                    <li><a href="tables-datatable.html">Data Table</a></li>
                                    <li><a href="tables-responsive.html">Responsive Table</a></li>
                                    <li><a href="tables-editable.html">Editable Table</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-album"></i> <span> Icons  <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span></span> </a>
                                <ul class="submenu">
                                    <li><a href="icons-material.html">Material Design</a></li>
                                    <li><a href="icons-ion.html">Ion Icons</a></li>
                                    <li><a href="icons-fontawesome.html">Font Awesome</a></li>
                                    <li><a href="icons-themify.html">Themify Icons</a></li>
                                    <li><a href="icons-dripicons.html">Dripicons</a></li>
                                    <li><a href="icons-typicons.html">Typicons Icons</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="calendar.html" class="waves-effect"><i class="mdi mdi-calendar-check"></i><span> Calendar </span></a>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-google-maps"></i><span> Maps  <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span></span></a>
                                <ul class="submenu">
                                    <li><a href="maps-google.html"> Google Map</a></li>
                                    <li><a href="maps-vector.html"> Vector Map</a></li>
                                </ul>
                            </li>

                            <li class="menu-title">Extras</li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-page-layout-sidebar-left"></i><span> Layouts <span class="badge badge-warning float-right">NEW</span> </span></a>
                                <ul class="submenu">
                                    <li><a href="layouts-dark-sidebar.html">Dark Sidebar</a></li>
                                    <li><a href="layouts-sidebar-user.html">Sidebar with User</a></li>
                                    <li><a href="layouts-collapsed.html">Collpased Sidenav</a></li>
                                    <li><a href="layouts-small.html">Small Sidebar</a></li>
                                    <li><a href="layouts-title2.html">Page Title 2</a></li>
                                </ul>
                            </li>

                            <li>
                                <a href="javascript:void(0);" class="waves-effect"><i class="mdi mdi-google-pages"></i><span> Pages <span class="float-right menu-arrow"><i class="mdi mdi-plus"></i></span> </span></a>
                                <ul class="submenu">
                                    <li><a href="pages-login.html">Login</a></li>
                                    <li><a href="pages-register.html">Register</a></li>
                                    <li><a href="pages-recoverpw.html">Recover Password</a></li>
                                    <li><a href="pages-lock-screen.html">Lock Screen</a></li>
                                    <li><a href="pages-timeline.html">Timeline</a></li>
                                    <li><a href="pages-invoice.html">Invoice</a></li>
                                    <li><a href="pages-directory.html">Directory</a></li>
                                    <li><a href="pages-blank.html">Blank Page</a></li>
                                    <li><a href="pages-404.html">Error 404</a></li>
                                    <li><a href="pages-500.html">Error 500</a></li>
                                </ul>
                            </li>
                        </ul>

                    </div>
                    <!-- Sidebar -->
                    <div class="clearfix"></div>

                </div>
                <!-- Sidebar -left -->

            </div>
            <!-- Left Sidebar End -->

            <!-- ============================================================== -->
            <!-- Start right Content here -->
            <!-- ============================================================== -->
            <div class="content-page">
                <!-- Start content -->
                <div class="content">
                    <div class="container-fluid">

                        <div class="row">
                            <div class="col-sm-12">
                                <div class="page-title-box">
                                    <h4 class="page-title">Dashboard</h4>
                                    <ol class="breadcrumb">
                                        <li class="breadcrumb-item active">Welcome to social media monitor for crisis</li>
                                    </ol>
                                </div>
                            </div>
                        </div>
                        <!-- end row -->

                        <div class="page-content-wrapper">
                            <div class="row">
                                <div class="col-xl-3 col-md-6">
                                    <div class="card bg-primary mini-stat position-relative">
                                        <div class="card-body">
                                            <div class="mini-stat-desc">
                                                <h6 class="text-uppercase verti-label text-white-50">受灾人数</h6>
                                                <div class="text-white">
                                                    <h6 class="text-uppercase mt-0 text-white-50">2019年受灾人数</h6>
                                                    <h3 class="mb-3 mt-0">1.3亿人次</h3>
                                                    <div class="">
                                                        <span class="badge badge-light text-info"> -25% </span> <span class="ml-2">相对五年均值</span>
                                                    </div>
                                                </div>
                                                <div class="mini-stat-icon">
                                                    <i class="mdi mdi-cube-outline display-2"></i>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-3 col-md-6">
                                    <div class="card bg-primary mini-stat position-relative">
                                        <div class="card-body">
                                            <div class="mini-stat-desc">
                                                <h6 class="text-uppercase verti-label text-white-50">灾难造成的经济损失</h6>
                                                <div class="text-white">
                                                    <h6 class="text-uppercase mt-0 text-white-50">2019年经济损失</h6>
                                                    <h3 class="mb-3 mt-0">3270.9亿</h3>
                                                    <div class="">
                                                        <span class="badge badge-light text-info"> -24% </span> <span class="ml-2">相对五年均值</span>
                                                    </div>
                                                </div>
                                                <div class="mini-stat-icon">
                                                    <i class="mdi mdi-buffer display-2"></i>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-3 col-md-6">
                                    <div class="card bg-primary mini-stat position-relative">
                                        <div class="card-body">
                                            <div class="mini-stat-desc">
                                                <h6 class="text-uppercase verti-label text-white-50">灾难中的房屋倒塌数</h6>
                                                <div class="text-white">
                                                    <h6 class="text-uppercase mt-0 text-white-50">2019年房屋倒塌数</h6>
                                                    <h3 class="mb-3 mt-0">12.6万间</h3>
                                                    <div class="">
                                                        <span class="badge badge-light text-info"> -57% </span> <span class="ml-2">相对五年均值</span>
                                                    </div>
                                                </div>
                                                <div class="mini-stat-icon">
                                                    <i class="mdi mdi-buffer display-2"></i>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
								<div class="col-xl-3 col-md-6">
                                    <div class="card bg-primary mini-stat position-relative">
                                        <div class="card-body">
                                            <div class="mini-stat-desc">
                                                <h6 class="text-uppercase verti-label text-white-50">微博活跃用户</h6>
                                                <div class="text-white">
                                                    <h6 class="text-uppercase mt-0 text-white-50">2019年底微博月活跃人数</h6>
                                                    <h3 class="mb-3 mt-0">5.16亿</h3>
                                                    <div class="">
                                                        <span class="badge badge-light text-info"> +5400万 </span> <span class="ml-2">相对2018年底</span>
                                                    </div>
                                                </div>
                                                <div class="mini-stat-icon">
                                                    <i class="mdi mdi-buffer display-2"></i>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end row -->
                            
                            <div class="row">
                                <div class="col-xl-9">
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col-xl-8 border-right">
                                                    <h4 class="mt-0 header-title mb-4">灾难相关的微博数量</h4>
                                                    <div id="morris-area-example" class="dashboard-charts morris-charts"></div>
                                                </div>
                                                <div class="col-xl-4">
                                                    <h4 class="header-title mb-4">系统功能</h4>
                                                    <div class="p-3">
                                                        <ul class="nav nav-pills nav-justified mb-3" role="tablist">
                                                            <li class="nav-item">
                                                                <a class="nav-link active" id="pills-first-tab" data-toggle="pill" href="#pills-first" role="tab" aria-controls="pills-first" aria-selected="true">地图标注</a>
                                                            </li>
                                                            <li class="nav-item">
                                                                <a class="nav-link" id="pills-second-tab" data-toggle="pill" href="#pills-second" role="tab" aria-controls="pills-second" aria-selected="false">历史文本</a>
                                                            </li>
                                                            <li class="nav-item">
                                                                <a class="nav-link" id="pills-third-tab" data-toggle="pill" href="#pills-third" role="tab" aria-controls="pills-third" aria-selected="false">数据统计</a>
                                                            </li>
                                                        </ul>
                                                        
                                                        <div class="tab-content">
                                                            <div class="tab-pane show active" id="pills-first" role="tabpanel" aria-labelledby="pills-first-tab">
                                                                <div class="p-3">
                                                                    <p class="text-muted">受灾地点将以地图标注的方式进行可视化，同时微博原文和分析后的数据也将进行展示。该功能基于百度地图进行开发。</p>
                                                                </div>
                                                            </div>
                                                            <div class="tab-pane" id="pills-second" role="tabpanel" aria-labelledby="pills-second-tab">
                                                                <div class="p-3">
                                                                    <p class="text-muted">系统会收集灾难相关的微博原文，并予以展示。同时，文本分类的结果将与微博原文同时展示。</p>
                                                                </div>
                                                            </div>
                                                            <div class="tab-pane" id="pills-third" role="tabpanel" aria-labelledby="pills-third-tab">
                                                                <div class="p-3">
                                                                    <p class="text-muted">通过对微博原文的分类和分析，很多统计信息可以从中提取出，如用户对某灾难的关注程度等。</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- end row -->
                                        </div>
                                    </div>
                                </div>
                                <!-- end col -->
                                
                                <div class="col-xl-3">
                                    <div class="card">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-4">Sales Analytics</h4>
                                            <div id="morris-donut-example" class="dashboard-charts morris-charts"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end row -->
                            
                            <div class="row">
                                <div class="col-xl-4">
                                    <div class="card m-b-20">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-3">Inbox</h4>
                                            <div class="inbox-wid">
                                                <a href="#" class="text-dark">
                                                    <div class="inbox-item">
                                                        <div class="inbox-item-img float-left mr-3"><img src="assets/images/users/user-1.jpg" class="thumb-md rounded-circle" alt=""></div>
                                                        <h6 class="inbox-item-author mt-0 mb-1">Irene</h6>
                                                        <p class="inbox-item-text text-muted mb-0">Hey! there I'm available...</p>
                                                        <p class="inbox-item-date text-muted">13:40 PM</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="text-dark">
                                                    <div class="inbox-item">
                                                        <div class="inbox-item-img float-left mr-3"><img src="assets/images/users/user-2.jpg" class="thumb-md rounded-circle" alt=""></div>
                                                        <h6 class="inbox-item-author mt-0 mb-1">Jennifer</h6>
                                                        <p class="inbox-item-text text-muted mb-0">I've finished it! See you so...</p>
                                                        <p class="inbox-item-date text-muted">13:34 PM</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="text-dark">
                                                    <div class="inbox-item">
                                                        <div class="inbox-item-img float-left mr-3"><img src="assets/images/users/user-3.jpg" class="thumb-md rounded-circle" alt=""></div>
                                                        <h6 class="inbox-item-author mt-0 mb-1">Richard</h6>
                                                        <p class="inbox-item-text text-muted mb-0">This theme is awesome!</p>
                                                        <p class="inbox-item-date text-muted">13:17 PM</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="text-dark">
                                                    <div class="inbox-item">
                                                        <div class="inbox-item-img float-left mr-3"><img src="assets/images/users/user-4.jpg" class="thumb-md rounded-circle" alt=""></div>
                                                        <h6 class="inbox-item-author mt-0 mb-1">Martin</h6>
                                                        <p class="inbox-item-text text-muted mb-0">Nice to meet you</p>
                                                        <p class="inbox-item-date text-muted">12:20 PM</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="text-dark">
                                                    <div class="inbox-item">
                                                        <div class="inbox-item-img float-left mr-3"><img src="assets/images/users/user-5.jpg" class="thumb-md rounded-circle" alt=""></div>
                                                        <h6 class="inbox-item-author mt-0 mb-1">Sean</h6>
                                                        <p class="inbox-item-text text-muted mb-0">Hey! there I'm available...</p>
                                                        <p class="inbox-item-date text-muted">11:47 AM</p>
                                                    </div>
                                                </a>
                                                
                                            </div>  
                                        </div>
                                    </div>

                                </div>
                                <div class="col-xl-4">
                                    <div class="card">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-5">Recent Activity Feed</h4>
                                            <div>
                                                <ul class="nav nav-pills nav-justified recent-activity-tab mb-4" id="recent-activity-tab" role="tablist">
                                                    <li class="nav-item">
                                                        <a class="nav-link active" id="activity1-tab" data-toggle="pill" href="#activity1" role="tab" aria-controls="activity1" aria-selected="true">21 Sep</a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a class="nav-link" id="activity2-tab" data-toggle="pill" href="#activity2" role="tab" aria-controls="activity2" aria-selected="false">22 Sep</a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a class="nav-link" id="activity3-tab" data-toggle="pill" href="#activity3" role="tab" aria-controls="activity3" aria-selected="false">23 Sep</a>
                                                    </li>
                                                    <li class="nav-item">
                                                        <a class="nav-link" id="activity4-tab" data-toggle="pill" href="#activity4" role="tab" aria-controls="activity4" aria-selected="false">24 Sep</a>
                                                    </li>
                                                </ul>
                                                <div class="tab-content">
                                                    <div class="tab-pane show active" id="activity1" role="tabpanel" aria-labelledby="activity1-tab">
                                                        <div class="p-3">
                                                            <div class="text-muted">
                                                                <p>21 Sep, 2018</p>
                                                                <h6 class="text-dark">Responded to need “Volunteer Activities”</h6>
                                                                <p>Aenean vulputate eleifend tellus</p>
                                                                <p>Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus Nullam quis ante.</p>
                                                                <a href="#" class="text-primary">Read More...</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="tab-pane" id="activity2" role="tabpanel" aria-labelledby="activity2-tab">
                                                        <div class="p-3">
                                                            <div class="text-muted">
                                                                <p>22 Sep, 2018</p>
                                                                <h6 class="text-dark">Added an interest “Volunteer Activities”</h6>
                                                                <p>Neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur velit sed quia non tempora incidunt.</p>
                                                                <p>Ut enim ad minima veniam quis nostrum</p>
                                                                <a href="#" class="text-primary">Read More...</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="tab-pane" id="activity3" role="tabpanel" aria-labelledby="activity3-tab">
                                                        <div class="p-3">
                                                            <div class="text-muted">
                                                                <p>23 Sep, 2018</p>
                                                                <h6 class="text-dark">Joined the group “Boardsmanship Forum”</h6>
                                                                <p>Nemo enim voluptatem quia voluptas</p>
                                                                <p>Donec pede justo fringilla vel aliquet nec vulputate eget arcu. In enim justo rhoncus ut imperdiet a venenatis vitae. </p>
                                                                <a href="#" class="text-primary">Read More...</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="tab-pane" id="activity4" role="tabpanel" aria-labelledby="activity4-tab">
                                                        <div class="p-3">
                                                            <div class="text-muted">
                                                                <p>24 Sep, 2018</p>
                                                                <h6 class="text-dark">Attending the event “Some New Event”</h6>
                                                                <p>At vero eos et accusamus et iusto odio</p>
                                                                <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium </p>
                                                                <a href="#" class="text-primary">Read More...</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4">
                                    <div class="card">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-4">Top product sales</h4>
                                            <div class="table-responsive">
                                                <table class="table table-hover mb-0">
                                                    <tbody>
                                                        <tr>
                                                            <td>
                                                                <h6 class="mt-0">Computers</h6>
                                                                <p class="text-muted mb-0">The languages only differ</p>
                                                            </td>
                                                            <td>
                                                                <div>
                                                                    <span class="peity-pie" data-peity='{ "fill": ["#f16c69", "#f2f2f2"]}' data-width="54" data-height="54">70/100</span>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <h6 class="mt-0">70%</h6>
                                                                <p class="text-muted mb-0">Sales</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>
                                                                <h6 class="mt-0">Laptops</h6>
                                                                <p class="text-muted mb-0">Maecenas tempus tellus</p>
                                                            </td>
                                                            <td>
                                                                <div>
                                                                    <span class="peity-donut" data-peity='{ "fill": ["#28bbe3", "#f2f2f2"], "innerRadius": 20, "radius": 32 }' data-width="54" data-height="54">9,4</span>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <h6 class="mt-0">84%</h6>
                                                                <p class="text-muted mb-0">Sales</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>
                                                                <h6 class="mt-0">Ipad</h6>
                                                                <p class="text-muted mb-0">Donec pede justo</p>
                                                            </td>
                                                            <td>
                                                                <div>
                                                                    <span class="peity-pie" data-peity='{ "fill": ["#f16c69", "#f2f2f2"]}' data-width="54" data-height="54">62/100</span>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <h6 class="mt-0">62%</h6>
                                                                <p class="text-muted mb-0">Sales</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>
                                                                <h6 class="mt-0">Mobile</h6>
                                                                <p class="text-muted mb-0">Aenean leo ligula</p>
                                                            </td>
                                                            <td>
                                                                <div>
                                                                    <span class="peity-donut" data-peity='{ "fill": ["#28bbe3", "#f2f2f2"], "innerRadius": 20, "radius": 32 }' data-width="54" data-height="54">20,4</span>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <h6 class="mt-0">89%</h6>
                                                                <p class="text-muted mb-0">Sales</p>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
    
                            </div>
                            <!-- end row -->

                            <div class="row">
                                <div class="col-xl-6">
                                    <div class="card">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-4">Latest Trasaction</h4>
                                            <div class="table-responsive">
                                                <table class="table table-hover mb-0">
                                                    <thead>
                                                      <tr>
                                                        <th scope="col">(#) Id</th>
                                                        <th scope="col">Name</th>
                                                        <th scope="col">Date</th>
                                                        <th scope="col">Amount</th>
                                                        <th scope="col" colspan="2">Status</th>
                                                      </tr>
                                                    </thead>
                                                    <tbody>
                                                      <tr>
                                                        <th scope="row">#15236</th>
                                                        <td>
                                                            <div>
                                                                <img src="assets/images/users/user-2.jpg" alt="" class="thumb-md rounded-circle mr-2"> Jeanette James
                                                            </div>
                                                        </td>
                                                        <td>14/8/2018</td>
                                                        <td>$104</td>
                                                        <td><span class="badge badge-success">Delivered</span></td>
                                                        <td>
                                                            <div>
                                                                <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                            </div>
                                                        </td>
                                                      </tr>
                                                      <tr>
                                                        <th scope="row">#15237</th>
                                                        <td>
                                                            <div>
                                                                <img src="assets/images/users/user-3.jpg" alt="" class="thumb-md rounded-circle mr-2"> Christopher Taylor
                                                            </div>
                                                        </td>
                                                        <td>15/8/2018</td>
                                                        <td>$112</td>
                                                        <td><span class="badge badge-warning">Pending</span></td>
                                                        <td>
                                                            <div>
                                                                <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                            </div>
                                                        </td>
                                                      </tr>
                                                      <tr>
                                                        <th scope="row">#15238</th>
                                                        <td>
                                                            <div>
                                                                <img src="assets/images/users/user-4.jpg" alt="" class="thumb-md rounded-circle mr-2"> Edward Vazquez
                                                            </div>
                                                        </td>
                                                        <td>15/8/2018</td>
                                                        <td>$116</td>
                                                        <td><span class="badge badge-success">Delivered</span></td>
                                                        <td>
                                                            <div>
                                                                <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                            </div>
                                                        </td>
                                                      </tr>
                                                      <tr>
                                                        <th scope="row">#15239</th>
                                                        <td>
                                                            <div>
                                                                <img src="assets/images/users/user-5.jpg" alt="" class="thumb-md rounded-circle mr-2"> Michael Flannery
                                                            </div>
                                                        </td>
                                                        <td>16/8/2018</td>
                                                        <td>$109</td>
                                                        <td><span class="badge badge-primary">Cancel</span></td>
                                                        <td>
                                                            <div>
                                                                <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                            </div>
                                                        </td>
                                                      </tr>
                                                      <tr>
                                                        <th scope="row">#15240</th>
                                                        <td>
                                                            <div>
                                                                <img src="assets/images/users/user-6.jpg" alt="" class="thumb-md rounded-circle mr-2"> Jamie Fishbourne
                                                            </div>
                                                        </td>
                                                        <td>17/8/2018</td>
                                                        <td>$120</td>
                                                        <td><span class="badge badge-success">Delivered</span></td>
                                                        <td>
                                                            <div>
                                                                <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                            </div>
                                                        </td>
                                                      </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-6">
                                    <div class="card">
                                        <div class="card-body">
                                            <h4 class="mt-0 header-title mb-4">Latest Order</h4>
                                            <div class="table-responsive order-table">
                                                <table class="table table-hover mb-0">
                                                    <thead>
                                                        <tr>
                                                        <th scope="col">(#) Id</th>
                                                        <th scope="col">Name</th>
                                                        <th scope="col">Date/Time</th>
                                                        <th scope="col">Amount</th>
                                                        <th scope="col" colspan="2">Status</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th scope="row">#14562</th>
                                                            <td>
                                                                <div>
                                                                    <img src="assets/images/users/user-4.jpg" alt="" class="thumb-md rounded-circle mr-2"> Matthew Drapeau
                                                                </div>
                                                            </td>
                                                            <td>17/8/2018
                                                                <p class="font-13 text-muted mb-0">8:26AM</p>
                                                            </td>
                                                            <td>$104</td>
                                                            <td><span class="badge badge-success badge-pill"><i class="mdi mdi-checkbox-blank-circle text-success"></i> Delivered</span></td>
                                                            <td>
                                                                <div>
                                                                    <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <th scope="row">#14563</th>
                                                            <td>
                                                                <div>
                                                                    <img src="assets/images/users/user-5.jpg" alt="" class="thumb-md rounded-circle mr-2"> Ralph Shockey
                                                                </div>
                                                            </td>
                                                            <td>18/8/2018
                                                                <p class="font-13 text-muted mb-0">10:18AM</p>
                                                            </td>
                                                            <td>$112</td>
                                                            <td><span class="badge badge-warning badge-pill"><i class="mdi mdi-checkbox-blank-circle text-warning"></i> Pending</span></td>
                                                            <td>
                                                                <div>
                                                                    <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <th scope="row">#14564</th>
                                                            <td>
                                                                <div>
                                                                    <img src="assets/images/users/user-6.jpg" alt="" class="thumb-md rounded-circle mr-2"> Alexander Pierson
                                                                </div>
                                                            </td>
                                                            <td>18//8/2018
                                                                <p class="font-13 text-muted mb-0">12:36PM</p>
                                                            </td>
                                                            <td>$116</td>
                                                            <td><span class="badge badge-success badge-pill"><i class="mdi mdi-checkbox-blank-circle text-success"></i> Delivered</span></td>
                                                            <td>
                                                                <div>
                                                                    <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <th scope="row">#14565</th>
                                                            <td>
                                                                <div>
                                                                    <img src="assets/images/users/user-7.jpg" alt="" class="thumb-md rounded-circle mr-2"> Robert Rankin
                                                                </div>
                                                            </td>
                                                            <td>19/8/2018
                                                                <p class="font-13 text-muted mb-0">11:47AM</p>
                                                            </td>
                                                            <td>$109</td>
                                                            <td><span class="badge badge-primary badge-pill"><i class="mdi mdi-checkbox-blank-circle text-primary"></i> Cancel</span></td>
                                                            <td>
                                                                <div>
                                                                    <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <th scope="row">#14566</th>
                                                            <td>
                                                                <div>
                                                                    <img src="assets/images/users/user-8.jpg" alt="" class="thumb-md rounded-circle mr-2"> Myrna Shields
                                                                </div>
                                                            </td>
                                                            <td>20/8/2018
                                                                <p class="font-13 text-muted mb-0">02:52PM</p>
                                                            </td>
                                                            <td>$120</td>
                                                            <td><span class="badge badge-success badge-pill"><i class="mdi mdi-checkbox-blank-circle text-success"></i> Delivered</span></td>
                                                            <td>
                                                                <div>
                                                                    <a href="#" class="btn btn-primary btn-sm">Edit</a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

        
                        </div>
                        <!-- end page content-->

                    </div> <!-- container-fluid -->

                </div> <!-- content -->

                <footer class="footer">
                    © 2018 Agroxa <span class="d-none d-sm-inline-block">- Crafted with <i class="mdi mdi-heart text-danger"></i> by Themesbrand.</span>
                </footer>

            </div>


            <!-- ============================================================== -->
            <!-- End Right content here -->
            <!-- ============================================================== -->


        </div>
        <!-- END wrapper -->
            

        <!-- jQuery  -->
        <script src="../js/jquery.min.js"></script>
        <script src="../js/bootstrap.bundle.min.js"></script>
        <script src="../js/metisMenu.min.js"></script>
        <script src="../js/jquery.slimscroll.js"></script>
        <script src="../js/waves.min.js"></script>

        <script src="../../../plugins/jquery-sparkline/jquery.sparkline.min.js"></script>

        <!-- Peity JS -->
        <script src="../../../plugins/peity/jquery.peity.min.js"></script>

        <script src="../../../plugins/morris/morris.min.js"></script>
        <script src="../../../plugins/raphael/raphael-min.js"></script>
		<script src="./dashboard.js"></script>

        <!-- App js -->
        <script src="../js/app.js"></script>

		<?php
			class MyDB extends SQLite3{
				function __construct(){
					$this->open('/home/web/qiuyi/SMASAC/.spyproject/data.db');
				}
			}
			$sql1 = "SELECT substr(time,0,8) as time, count(*) as count from earthquake_originaltext group by substr(time,0,8)";
			$sql2 = "SELECT substr(time,0,8) as time, count(*) as count from typhoon_originaltext group by substr(time,0,8)";
			$sql3 = "SELECT substr(time,0,8) as time, count(*) as count from rainstorm_originaltext group by substr(time,0,8)";

			$db = new MyDB();
			$ret1 = $db->query($sql1);
			$ret2 = $db->query($sql2);
			$ret3 = $db->query($sql3);

			$count1=array();
			$count2=array();
			$count3=array();

			$time1=array();
			$time2=array();
			$time3=array();

			$tot=0;
			if(!$ret1){
				echo $db->lastErrorMsg();
			}
			else{
				while($row = $ret1->fetchArray(SQLITE3_ASSOC)){
					$count1[]=(int)$row['count'];
					$time1[]=$row['time'];
				}
			}

			if(!$ret2){
				echo $db->lastErrorMsg();
			}
			else{
				while($row = $ret2->fetchArray(SQLITE3_ASSOC)){
					$count2[]=(int)$row['count'];
					$time2[]=$row['time'];
				}
			}

			if(!$ret3){
				echo $db->lastErrorMsg();
			}
			else{
				while($row = $ret3->fetchArray(SQLITE3_ASSOC)){
					$count3[]=(int)$row['count'];
					$time3[]=$row['time'];
				}
			}

			$data=array();

			for($x=0;$x<count($count2);$x++){
				$data[]=array('y'=>$time1[$x+1],'a'=>$count1[$x+1],'b'=>$count2[$x],'c'=>$count3[$x]);
			}

			$countjson1=json_encode($count1);
			$countjson2=json_encode($count2);
			$countjson3=json_encode($count3);

			$timejson1=json_encode($time1);
			$timejson2=json_encode($time2);
			$timejson3=json_encode($time3);

			$datajson=json_encode($data);

			echo "<script language='javascript'>
					var count1=$countjson1;
					var count2=$countjson2;
					var count3=$countjson3;

					var time1=$timejson1;
					var time2=$timejson2;
					var time3=$timejson3;
					
					var data=$datajson;
			</script>";	
		?>

		<script language='javascript'>
			!function($) {
				"use strict";

				var Dashboard = function() {};
				
				//creates area chart
				Dashboard.prototype.createAreaChart = function (element, pointSize, lineWidth, data, xkey, ykeys, labels, lineColors) {
					Morris.Area({
						element: element,
						pointSize: 0,
						lineWidth: 0,
						data: data,
						xkey: xkey,
						ykeys: ykeys,
						labels: labels,
						resize: true,
						gridLineColor: '#eee',
						hideHover: 'auto',
						lineColors: lineColors,
						fillOpacity: .7,
						behaveLikeLine: true
					});
				},

				//creates Donut chart
				Dashboard.prototype.createDonutChart = function (element, data, colors) {
					Morris.Donut({
						element: element,
						data: data,
						resize: true,
						colors: colors
					});
				},

				 //pie
					$('.peity-pie').each(function () {
						$(this).peity("pie", $(this).data());
					});

					//donut
					$('.peity-donut').each(function () {
						$(this).peity("donut", $(this).data());
					});

			  
				
				Dashboard.prototype.init = function() {
					
					//creating area chart
					//var $areaData = [
					//	{y: '2011', a: 0, b: 0, c:0},
					//	{y: '2012', a: 150, b: 45, c:15},
					//	{y: '2013', a: 60, b: 150, c:195},
					//	{y: '2014', a: 180, b: 36, c:21},
					//	{y: '2015', a: 90, b: 60, c:360},
					//	{y: '2016', a: 75, b: 240, c:120},
					//	{y: '2017', a: 30, b: 30, c:30}
					//];
					var $areaData=datajson;
					this.createAreaChart('morris-area-example', 0, 0, $areaData, 'y', ['a', 'b', 'c'], ['地震', '台风', '暴雨'], ['#ccc', '#f16c69', '#28bbe3']);

					//creating donut chart
					var $donutData = [
						{label: "Download Sales", value: 12},
						{label: "In-Store Sales", value: 30},
						{label: "Mail-Order Sales", value: 20}
					];
					this.createDonutChart('morris-donut-example', $donutData, ['#f0f1f4', '#f16c69', '#28bbe3']);

				},
				//init
				$.Dashboard = new Dashboard, $.Dashboard.Constructor = Dashboard
			}(window.jQuery),

			//initializing 
			function($) {
				"use strict";
				$.Dashboard.init();
			}(window.jQuery);

		</script>

    </body>

</html>