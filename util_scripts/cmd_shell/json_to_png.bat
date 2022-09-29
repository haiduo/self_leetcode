@echo off 
rem 启用"延缓环境变量扩充" 
setlocal EnableDelayedExpansion 
set a=0 
cd
rem 循环input目录下所有json的文件名，支持带空格的名称 
for %%i in (input_1\*.json) do (
    echo %%i
    rem 依据文件名称创建文件夹 
    labelme_json_to_dataset %%i  -o  output\%%~ni
    move output\%%~ni\img.png output_image\%%~ni.png
    move output\%%~ni\label.png output_label\%%~ni.png
    move output\%%~ni\label_viz.png output_vision\%%~ni.png
    set /a a+=1 
) 
echo all %a% finish !
pause