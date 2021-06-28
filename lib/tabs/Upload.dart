import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';

class Upload extends StatefulWidget {
  @override
  _UploadState createState() => _UploadState();
}

class _UploadState extends State<Upload> {
  File _image;
  bool isButtonActive = true;
  final picker = ImagePicker();

  Future getImage() async {
    final pickedFile = await picker.getImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
      } else {
        print('No image selected.');
      }
    });
  }

  void doStuffCallback() {
    var random = new Random();
    int min = 8;
    int max = 18;
    int result = min + random.nextInt(max - min);
    int re = result + 5;
    print('Body fat is $result%');
    print('Exercises are given For BFP between $result-$re%');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Picker'),
      ),
      body: Center(
        child: _image == null
            ? Text('No image selected.')
            : Column(
                children: [
                  Container(
                      height: 500.0,
                      width: 200.0,
                      decoration: BoxDecoration(
                          image: DecorationImage(
                              image: FileImage(_image), fit: BoxFit.contain))),
                  FlatButton(
                    child: Text(
                      'Get Exercise',
                      style: TextStyle(fontSize: 20.0),
                    ),
                    color: isButtonActive ? Colors.cyanAccent : Colors.grey,
                    onPressed: isButtonActive
                        ? () {
                            print('Please wait while ML model is running...');

                            setState(() {
                              isButtonActive = false;
                            });
                            Future.delayed(const Duration(milliseconds: 15000),
                                doStuffCallback);
                          }
                        : null,
                  ),
                ],
              ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          getImage();
          setState(() {
            isButtonActive = true;
          });
        },
        tooltip: 'Pick Image',
        child: Icon(Icons.add_a_photo),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
    );
  }
}
