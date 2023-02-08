<h1 align="center"> Virtual assistant </h1>

### Description
Many people and companies are looking for ways to improve their productivity, efficiency and reduce costs. Whether for example by automating repetitive or precise tasks.
And one of the tools that can facilitate these types of processes is a virtual assistant, since it may be able to understand and generate natural language effectively. Using machine learning algorithms and artificial intelligence capable of making decisions and responding to different situations.
You can also integrate the virtual assistant with other systems, such as databases, calendar applications, email, etc. This can be achieved by using APIs and other means to connect different systems.

That is why I decided to create an interactive and fun virtual assistant, in order to entertain and cheer up the user who wants to use it.
It has 2 security methods implemented with it, one for voice recognition, and the other for facial recognition, it is necessary to pass both security filters in order to have access to all the tools that the virtual assistant can provide.

The user can connect their email, facebook, whatsapp, among other social networks or applications.
The user can ask general culture questions.
The user can take photos and apply any of the different styles implemented in the virtual assistant.


<div align="center">
    <img src="./main_features/images/readme_images/Screenshot from 2023-02-07 12-58-59.png">
    <img src="./main_features/images/readme_images/Screenshot from 2023-02-07 13-00-17.png">
    <img src="./main_features/images/readme_images/Screenshot from 2023-02-07 13-01-38.png">
</div>

### Dependencies

<a href="https://openai.com/api/">Create an account in OPENAI and get the API to connect to the project </a>

<a href="https://alphacephei.com/vosk/models">Dowload VOSK model and place it inside the folder **./main_features**</a>

```
pip install -r requirements.txt
```

### Usage

Go to folder **main_features** and run:


```
./vosk_va_english.py
```

### Citing resources used

```bibtex
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}

```
### References

https://arxiv.org/abs/1705.06830
https://openaccess.thecvf.com/content/CVPR2021/html/Kotovenko_Rethinking_Style_Transfer_From_Pixels_to_Parameterized_Brushstrokes_CVPR_2021_paper.html
https://arxiv.org/abs/1705.06830
https://arxiv.org/pdf/2104.01541v2.pdf
https://arxiv.org/pdf/2010.10504v2.pdf
https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0


![image](https://imgs.search.brave.com/xFpLwryLJ7-hi1BPwJwcl9l8ZR8u4poviDaw84RB6dw/rs:fit:1200:720:1/g:ce/aHR0cHM6Ly9jb250/ZW50LmZvcnR1bmUu/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE2LzEyL2dhdGVi/b3gtaGlrYXJpLXlv/dXR1YmUuanBn)
