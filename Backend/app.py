from keras.models import load_model
import urllib.request
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# function varargout = Fat_Detect(varargin)
# % FAT_DETECT MATLAB code for Fat_Detect.fig
# %      FAT_DETECT, by itself, creates a new FAT_DETECT or raises the existing
# %      singleton*.
# %
# %      H = FAT_DETECT returns the handle to a new FAT_DETECT or the handle to
# %      the existing singleton*.
# %
# %      FAT_DETECT('CALLBACK',hObject,eventData,handles,...) calls the local
# %      function named CALLBACK in FAT_DETECT.M with the given input arguments.
# %
# %      FAT_DETECT('Property','Value',...) creates a new FAT_DETECT or raises the
# %      existing singleton*.  Starting from the left, property value pairs are
# %      applied to the GUI before Fat_Detect_OpeningFcn gets called.  An
# %      unrecognized property name or invalid value makes property application
# %      stop.  All inputs are passed to Fat_Detect_OpeningFcn via varargin.
# %
# %      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
# %      instance to run (singleton)".
# %
# % See also: GUIDE, GUIDATA, GUIHANDLES

# % Edit the above text to modify the response to help Fat_Detect

# % Last Modified by GUIDE v2.5 29-Mar-2021 21:15:23

# % Begin initialization code - DO NOT EDIT
# gui_Singleton = 1;
# gui_State = struct('gui_Name',       mfilename, ...
#                    'gui_Singleton',  gui_Singleton, ...
#                    'gui_OpeningFcn', @Fat_Detect_OpeningFcn, ...
#                    'gui_OutputFcn',  @Fat_Detect_OutputFcn, ...
#                    'gui_LayoutFcn',  [] , ...
#                    'gui_Callback',   []);
# if nargin && ischar(varargin{1})
#     gui_State.gui_Callback = str2func(varargin{1});
# end

# if nargout
#     [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
# else
#     gui_mainfcn(gui_State, varargin{:});
# end
# % End initialization code - DO NOT EDIT


# % --- Executes just before Fat_Detect is made visible.
# function Fat_Detect_OpeningFcn(hObject, eventdata, handles, varargin)
# % This function has no output args, see OutputFcn.
# % hObject    handle to figure
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)
# % varargin   command line arguments to Fat_Detect (see VARARGIN)

# % Choose default command line output for Fat_Detect
# handles.output = hObject;
# axes(handles.axes1); axis off
# axes(handles.axes2); axis off
# axes(handles.axes3); axis off
# axes(handles.axes4); axis off
# axes(handles.axes11); axis off
# axes(handles.axes12); axis off

# set(handles.edit2,'String','**');
# set(handles.edit3,'String','**');
# set(handles.edit4,'String','**');
# set(handles.edit5,'String','**');
# set(handles.edit6,'String','**');

# set(handles.edit20,'String','**');
# set(handles.edit21,'String','**');
# set(handles.edit22,'String','**');
# set(handles.edit23,'String','**');
# set(handles.edit24,'String','**');


# % Update handles structure
# guidata(hObject, handles);

# % UIWAIT makes Fat_Detect wait for user response (see UIRESUME)
# % uiwait(handles.figure1);


# % --- Outputs from this function are returned to the command line.
# function varargout = Fat_Detect_OutputFcn(hObject, eventdata, handles)
# % varargout  cell array for returning output args (see VARARGOUT);
# % hObject    handle to figure
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Get default command line output from handles structure
# varargout{1} = handles.output;


# % --- Executes on button press in pushbutton1.
# function pushbutton1_Callback(hObject, eventdata, handles)
# % hObject    handle to pushbutton1 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)
# global a;global skw;global ad;global m;global me; global img;  global img1; global image_Segment; global ddd;
# [fname,path]=uigetfile('*.*','Browse Image');
# if fname~=0
#     img=imread([path,fname]);
#     a=img;I=a;
#        axes(handles.axes1); imshow(img); title('Input Image');
# else
#     warndlg('Please Select the necessary Image File');
# end


# me=mean2(a);%mean
# sd=std2(a);%std dev
# en=entropy(a);%entropy
# skw=skewness(a(:));%skewness
# k=kurtosis(a(:));
# set(handles.edit2,'String',me);
# set(handles.edit3,'String',sd);
# set(handles.edit4,'String',en);
# set(handles.edit5,'String',k);
# set(handles.edit6,'String',skw);
# acc=accuracy_image(a);
# sen=Sensitivity_image(a);
# spe=specificity_image(a);
# set(handles.edit22,'String',acc );
# set(handles.edit23,'String',sen );
# set(handles.edit24,'String',spe);
#  % No faces at the beginning
# Faces=[];
# numFaceFound=0;

# I=double(I);

# H=size(I,1);
# W=size(I,2);
# R=I(:,:,1);
# G=I(:,:,2);
# B=I(:,:,3);

# %%%%%%%%%%%%%%%%%% LIGHTING COMPENSATION %%%%%%%%%%%%%%%
# YCbCr=rgb2ycbcr(I);
# Y=YCbCr(:,:,1);

# %normalize Y
# minY=min(min(Y));
# maxY=max(max(Y));
# Y=255.0*(Y-minY)./(maxY-minY);
# YEye=Y;
# Yavg=sum(sum(Y))/(W*H);

# T=1;
# if (Yavg<64)
#     T=1.4;
# elseif (Yavg>192)
#     T=0.6;
# end

# if (T~=1)
#     RI=R.^T;
#     GI=G.^T;
# else
#     RI=R;
#     GI=G;
# end

# C=zeros(H,W,3);
# C(:,:,1)=RI;
# C(:,:,2)=GI;
# C(:,:,3)=B;

# axes(handles.axes2); imshow(C/255);
# title('Lighting compensation');
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%%%%%%%%% EXTRACT SKIN %%%%%%%%%%%%%%%%%%%%%%
# YCbCr=rgb2ycbcr(C);
# Cr=YCbCr(:,:,3);

# S=zeros(H,W);
# [SkinIndexRow,SkinIndexCol] =find(10<Cr & Cr<45);
# for i=1:length(SkinIndexRow)
#     S(SkinIndexRow(i),SkinIndexCol(i))=1;
# end

# axes(handles.axes3); imshow(S);
# title('skin');
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%%% REMOVE NOISE %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SN=zeros(H,W);
# for i=1:H-5
#     for j=1:W-5
#         localSum=sum(sum(S(i:i+4, j:j+4)));
#         SN(i:i+5, j:j+5)=(localSum>12);
#     end
# end

# axes(handles.axes4); imshow(SN);
# title('skin with noise removal');
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# %%%%%%%%%%%%%%% FIND SKIN COLOR BLOCKS %%%%%%%%%%%%%%%%%

# L = bwlabel(SN,8);
# BB  = regionprops(L, 'BoundingBox');
# bboxes= cat(1, BB.BoundingBox);
# widths=bboxes(:,3);
# heights=bboxes(:,4);
# hByW=heights./widths;

# lenRegions=size(bboxes,1);
# foundFaces=zeros(1,lenRegions);

# rgb=label2rgb(L);
# axes(handles.axes11); imshow(rgb);
# title('face candidates');
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# %%%%%%%%%%%%%%%% CHECK FACE CRITERIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%

# for i=1:lenRegions

#     % 1st criteria: height to width ratio, computed above.
#     if (hByW(i)>1.75 || hByW(i)<0.75)
#         % this cannot be a mouth region. discard
#         continue;
#     end

#     % implemented by me: Impose a min face dimension constraint
#     if (heights(i)<20 && widths(i)<20)
#         continue;
#     end

#     % get current region's bounding box
#     CurBB=bboxes(i,:);
#     XStart=CurBB(1);
#     YStart=CurBB(2);
#     WCur=CurBB(3);
#     HCur=CurBB(4);

#     % crop current region
#     rangeY=int32(YStart):int32(YStart+HCur-1);
#     rangeX= int32(XStart):int32(XStart+WCur-1);
#     RIC=RI(rangeY, rangeX);
#     GIC=GI(rangeY, rangeX);
#     BC=B(rangeY, rangeX);

#     axes(handles.axes12);  imshow(RIC/255);
#     title('Possible face R channel');

#     % 2nd criteria: existance & localisation of mouth

#     M=zeros(HCur, WCur);

#     theta=acos( 0.5.*(2.*RIC-GIC-BC) ./ sqrt( (RIC-GIC).*(RIC-GIC) + (RIC-BC).*(GIC-BC) ) );
#     theta(isnan(theta))=0;
#     thetaMean=mean2(theta);
#     [MouthIndexRow,MouthIndexCol] =find(theta<thetaMean/4);
#     for j=1:length(MouthIndexRow)
#         M(MouthIndexRow(j),MouthIndexCol(j))=1;
#     end

#     % now compute vertical mouth histogram
#     Hist=zeros(1, HCur);

#     for j=1:HCur
#         Hist(j)=length(find(M(j,:)==1));
#     end

#     wMax=find(Hist==max(Hist));
#     wMax=wMax(1); % just take one of them.

#     if (wMax < WCur/6)
#         %reject due to not existing mouth
#         continue;
#     end

#     figure(), imshow(M);
#     title('Mouth map');

#     % 3rd criteria: existance & localisation of eyes

#     eyeH=HCur-wMax;
#     eyeW=WCur;

#     YC=YEye(YStart:YStart+eyeH-1, XStart:XStart+eyeW-1);

#     E=zeros(eyeH,eyeW);
#     [EyeIndexRow,EyeIndexCol] =find(65<YC & YC<80);
#     for j=1:length(EyeIndexRow)
#         E(EyeIndexRow(j),EyeIndexCol(j))=1;
#     end

#     % check if eyes are acceptable.
#     EyeExist=find(Hist>0.3*wMax);
#     if (~(length(EyeExist)>0))
#         continue;
#     end

#     foundFaces(i)=1;
#     numFaceFound=numFaceFound+1;

# end
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# disp('Number of faces found');
# numFaceFound;

# if (numFaceFound>0)
#     disp('Indices of faces found: ');
#     ind=find(foundFaces==1);
#     CurBB=bboxes(ind,:);
#     CurBB
# else
#     close all;
# end
# run('Find_Alg.m');


# % --- Executes on button press in pushbutton2.
# function pushbutton2_Callback(hObject, eventdata, handles)
# % hObject    handle to pushbutton2 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)
# close all


# % --- Executes on button press in pushbutton3.
# function pushbutton3_Callback(hObject, eventdata, handles)
# % hObject    handle to pushbutton3 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)
# axes(handles.axes1); cla(handles.axes1); title(''); axis off
# axes(handles.axes2); cla(handles.axes2); title(''); axis off
# axes(handles.axes3); cla(handles.axes3); title(''); axis off
# axes(handles.axes4); cla(handles.axes4); title(''); axis off
# axes(handles.axes11); cla(handles.axes11); title(''); axis off
# axes(handles.axes12); cla(handles.axes12); title(''); axis off

# set(handles.edit2,'String','---');
# set(handles.edit3,'String','---');
# set(handles.edit4,'String','---');
# set(handles.edit5,'String','---');
# set(handles.edit6,'String','---');
# set(handles.edit20,'String','---');
# set(handles.edit21,'String','---');
# set(handles.edit22,'String','---');
# set(handles.edit23,'String','---');
# set(handles.edit24,'String','---');


# % --- Executes on button press in pushbutton4.
# function pushbutton4_Callback(hObject, eventdata, handles)
# % hObject    handle to pushbutton4 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)
# % msgbox('LOAD THE DATASET....');
#  pause(2)
#  msgbox('INITIALIZATION....');
#  pause(2)
#  msgbox('CREATE THE DATABASE.....');
#  pause(2)

# for i=1:4
#     j=num2str(i);
#     imgname=strcat(j,'.png');
#     TrainData=imread(imgname);
#     TrainData=imresize(TrainData,[250 250]);
#     TrainData = im2double(TrainData);
# save database TrainData
# end
#  for i=8:13
#     j=num2str(i);
#     imgname=strcat(j,'.jpg');
#     TrainData=imread(imgname);
#     TrainData=imresize(TrainData,[250 250]);
#     TrainData = im2double(TrainData);
# save database TrainData
# end
#  msgbox('DATABASE SAVED SUCCESSFULLY....')
#  pause(2)
# model.save('Fat_Detect.m') converter = tf.lite.TFLiteConverter.from_keras_model( model )
# model = converter.convert() file = open( 'output.tflite' , 'wb' ) file.write( model )


# function edit1_Callback(hObject, eventdata, handles)
# % hObject    handle to edit1 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit1 as text
# %        str2double(get(hObject,'String')) returns contents of edit1 as a double


# % --- Executes during object creation, after setting all properties.
# function edit1_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit1 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit7_Callback(hObject, eventdata, handles)
# % hObject    handle to edit7 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit7 as text
# %        str2double(get(hObject,'String')) returns contents of edit7 as a double


# % --- Executes during object creation, after setting all properties.
# function edit7_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit7 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit8_Callback(hObject, eventdata, handles)
# % hObject    handle to edit8 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit8 as text
# %        str2double(get(hObject,'String')) returns contents of edit8 as a double


# % --- Executes during object creation, after setting all properties.
# function edit8_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit8 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit9_Callback(hObject, eventdata, handles)
# % hObject    handle to edit9 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit9 as text
# %        str2double(get(hObject,'String')) returns contents of edit9 as a double


# % --- Executes during object creation, after setting all properties.
# function edit9_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit9 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit10_Callback(hObject, eventdata, handles)
# % hObject    handle to edit10 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit10 as text
# %        str2double(get(hObject,'String')) returns contents of edit10 as a double


# % --- Executes during object creation, after setting all properties.
# function edit10_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit10 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit11_Callback(hObject, eventdata, handles)
# % hObject    handle to edit11 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit11 as text
# %        str2double(get(hObject,'String')) returns contents of edit11 as a double


# % --- Executes during object creation, after setting all properties.
# function edit11_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit11 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit2_Callback(hObject, eventdata, handles)
# % hObject    handle to edit2 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit2 as text
# %        str2double(get(hObject,'String')) returns contents of edit2 as a double


# % --- Executes during object creation, after setting all properties.
# function edit2_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit2 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit3_Callback(hObject, eventdata, handles)
# % hObject    handle to edit3 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit3 as text
# %        str2double(get(hObject,'String')) returns contents of edit3 as a double


# % --- Executes during object creation, after setting all properties.
# function edit3_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit3 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit4_Callback(hObject, eventdata, handles)
# % hObject    handle to edit4 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit4 as text
# %        str2double(get(hObject,'String')) returns contents of edit4 as a double


# % --- Executes during object creation, after setting all properties.
# function edit4_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit4 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit5_Callback(hObject, eventdata, handles)
# % hObject    handle to edit5 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit5 as text
# %        str2double(get(hObject,'String')) returns contents of edit5 as a double


# % --- Executes during object creation, after setting all properties.
# function edit5_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit5 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit6_Callback(hObject, eventdata, handles)
# % hObject    handle to edit6 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit6 as text
# %        str2double(get(hObject,'String')) returns contents of edit6 as a double


# % --- Executes during object creation, after setting all properties.
# function edit6_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit6 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# % --- Executes on selection change in listbox1.
# function listbox1_Callback(hObject, eventdata, handles)
# % hObject    handle to listbox1 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: contents = cellstr(get(hObject,'String')) returns listbox1 contents as cell array
# %        contents{get(hObject,'Value')} returns selected item from listbox1


# % --- Executes during object creation, after setting all properties.
# function listbox1_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to listbox1 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: listbox controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit12_Callback(hObject, eventdata, handles)
# % hObject    handle to edit12 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit12 as text
# %        str2double(get(hObject,'String')) returns contents of edit12 as a double


# % --- Executes during object creation, after setting all properties.
# function edit12_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit12 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit13_Callback(hObject, eventdata, handles)
# % hObject    handle to edit13 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit13 as text
# %        str2double(get(hObject,'String')) returns contents of edit13 as a double


# % --- Executes during object creation, after setting all properties.
# function edit13_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit13 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit14_Callback(hObject, eventdata, handles)
# % hObject    handle to edit14 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit14 as text
# %        str2double(get(hObject,'String')) returns contents of edit14 as a double


# % --- Executes during object creation, after setting all properties.
# function edit14_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit14 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit15_Callback(hObject, eventdata, handles)
# % hObject    handle to edit15 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit15 as text
# %        str2double(get(hObject,'String')) returns contents of edit15 as a double


# % --- Executes during object creation, after setting all properties.
# function edit15_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit15 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit16_Callback(hObject, eventdata, handles)
# % hObject    handle to edit16 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit16 as text
# %        str2double(get(hObject,'String')) returns contents of edit16 as a double


# % --- Executes during object creation, after setting all properties.
# function edit16_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit16 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit17_Callback(hObject, eventdata, handles)
# % hObject    handle to edit17 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit17 as text
# %        str2double(get(hObject,'String')) returns contents of edit17 as a double


# % --- Executes during object creation, after setting all properties.
# function edit17_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit17 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit18_Callback(hObject, eventdata, handles)
# % hObject    handle to edit18 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit18 as text
# %        str2double(get(hObject,'String')) returns contents of edit18 as a double


# % --- Executes during object creation, after setting all properties.
# function edit18_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit18 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit19_Callback(hObject, eventdata, handles)
# % hObject    handle to edit19 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit19 as text
# %        str2double(get(hObject,'String')) returns contents of edit19 as a double


# % --- Executes during object creation, after setting all properties.
# function edit19_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit19 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit30_Callback(hObject, eventdata, handles)
# % hObject    handle to edit30 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit30 as text
# %        str2double(get(hObject,'String')) returns contents of edit30 as a double


# % --- Executes during object creation, after setting all properties.
# function edit30_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit30 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end
# function edit31_Callback(hObject, eventdata, handles)
# % hObject    handle to edit31 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit31 as text
# %        str2double(get(hObject,'String')) returns contents of edit31 as a double


# % --- Executes during object creation, after setting all properties.
# function edit31_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit31 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit32_Callback(hObject, eventdata, handles)
# % hObject    handle to edit32 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit32 as text
# %        str2double(get(hObject,'String')) returns contents of edit32 as a double


# % --- Executes during object creation, after setting all properties.
# function edit32_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit32 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit33_Callback(hObject, eventdata, handles)
# % hObject    handle to edit33 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit33 as text
# %        str2double(get(hObject,'String')) returns contents of edit33 as a double


# % --- Executes during object creation, after setting all properties.
# function edit33_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit33 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit34_Callback(hObject, eventdata, handles)
# % hObject    handle to edit34 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit34 as text
# %        str2double(get(hObject,'String')) returns contents of edit34 as a double


# % --- Executes during object creation, after setting all properties.
# function edit34_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit34 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit25_Callback(hObject, eventdata, handles)
# % hObject    handle to edit25 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit25 as text
# %        str2double(get(hObject,'String')) returns contents of edit25 as a double


# % --- Executes during object creation, after setting all properties.
# function edit25_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit25 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit26_Callback(hObject, eventdata, handles)
# % hObject    handle to edit26 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit26 as text
# %        str2double(get(hObject,'String')) returns contents of edit26 as a double


# % --- Executes during object creation, after setting all properties.
# function edit26_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit26 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit27_Callback(hObject, eventdata, handles)
# % hObject    handle to edit27 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit27 as text
# %        str2double(get(hObject,'String')) returns contents of edit27 as a double


# % --- Executes during object creation, after setting all properties.
# function edit27_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit27 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit28_Callback(hObject, eventdata, handles)
# % hObject    handle to edit28 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit28 as text
# %        str2double(get(hObject,'String')) returns contents of edit28 as a double


# % --- Executes during object creation, after setting all properties.
# function edit28_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit28 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit29_Callback(hObject, eventdata, handles)
# % hObject    handle to edit29 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit29 as text
# %        str2double(get(hObject,'String')) returns contents of edit29 as a double


# % --- Executes during object creation, after setting all properties.
# function edit29_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit29 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit20_Callback(hObject, eventdata, handles)
# % hObject    handle to edit20 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit20 as text
# %        str2double(get(hObject,'String')) returns contents of edit20 as a double


# % --- Executes during object creation, after setting all properties.
# function edit20_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit20 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit21_Callback(hObject, eventdata, handles)
# % hObject    handle to edit21 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit21 as text
# %        str2double(get(hObject,'String')) returns contents of edit21 as a double


# % --- Executes during object creation, after setting all properties.
# function edit21_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit21 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit22_Callback(hObject, eventdata, handles)
# % hObject    handle to edit22 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit22 as text
# %        str2double(get(hObject,'String')) returns contents of edit22 as a double


# % --- Executes during object creation, after setting all properties.
# function edit22_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit22 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit23_Callback(hObject, eventdata, handles)
# % hObject    handle to edit23 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit23 as text
# %        str2double(get(hObject,'String')) returns contents of edit23 as a double


# % --- Executes during object creation, after setting all properties.
# function edit23_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit23 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit24_Callback(hObject, eventdata, handles)
# % hObject    handle to edit24 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit24 as text
# %        str2double(get(hObject,'String')) returns contents of edit24 as a double


# % --- Executes during object creation, after setting all properties.
# function edit24_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit24 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit35_Callback(hObject, eventdata, handles)
# % hObject    handle to edit35 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit35 as text
# %        str2double(get(hObject,'String')) returns contents of edit35 as a double


# % --- Executes during object creation, after setting all properties.
# function edit35_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit35 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit36_Callback(hObject, eventdata, handles)
# % hObject    handle to edit36 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit36 as text
# %        str2double(get(hObject,'String')) returns contents of edit36 as a double


# % --- Executes during object creation, after setting all properties.
# function edit36_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit36 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit37_Callback(hObject, eventdata, handles)
# % hObject    handle to edit37 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit37 as text
# %        str2double(get(hObject,'String')) returns contents of edit37 as a double


# % --- Executes during object creation, after setting all properties.
# function edit37_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit37 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit38_Callback(hObject, eventdata, handles)
# % hObject    handle to edit38 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit38 as text
# %        str2double(get(hObject,'String')) returns contents of edit38 as a double


# % --- Executes during object creation, after setting all properties.
# function edit38_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit38 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end


# function edit39_Callback(hObject, eventdata, handles)
# % hObject    handle to edit39 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    structure with handles and user data (see GUIDATA)

# % Hints: get(hObject,'String') returns contents of edit39 as text
# %        str2double(get(hObject,'String')) returns contents of edit39 as a double


# % --- Executes during object creation, after setting all properties.
# function edit39_CreateFcn(hObject, eventdata, handles)
# % hObject    handle to edit39 (see GCBO)
# % eventdata  reserved - to be defined in a future version of MATLAB
# % handles    empty - handles not created until after all CreateFcns called

# % Hint: edit controls usually have a white background on Windows.
# %       See ISPC and COMPUTER.
# if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
#     set(hObject,'BackgroundColor','white');
# end

api.add_resource(FatExtractor, '/')

if __name__ == '__main__':
    app.run()
