---
comments: true
---

# Seal Text Recognition Pipeline Tutorial

## 1. Introduction to Seal Text Recognition Pipeline
Seal text recognition is a technology that automatically extracts and recognizes the content of seals from documents or images. The recognition of seal text is part of document processing and has many applications in various scenarios, such as contract comparison, warehouse entry and exit review, and invoice reimbursement review.

The seal text recognition pipeline is used to recognize the text content of seals, extracting the text information from seal images and outputting it in text form. This pipeline integrates the industry-renowned end-to-end OCR system PP-OCRv4, supporting the detection and recognition of curved seal text. Additionally, this pipeline integrates an optional layout region localization module, which can accurately locate the layout position of the seal within the entire document. It also includes optional document image orientation correction and distortion correction functions. Based on this pipeline, millisecond-level accurate text content prediction can be achieved on a CPU. This pipeline also provides flexible service deployment methods, supporting the use of multiple programming languages on various hardware. Moreover, it offers secondary development capabilities, allowing you to train and fine-tune on your own dataset based on this pipeline, and the trained model can be seamlessly integrated.

<img src="https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/doc_images/practical_tutorial/PP-ChatOCRv3_doc_seal/01.png" style="width: 70%"/>
<b>The seal text recognition</b> pipeline includes a seal text detection module and a text recognition module, as well as optional layout detection module, document image orientation classification module, and text image correction module.

<b>If you prioritize model accuracy, choose a model with higher accuracy. If you prioritize inference speed, choose a model with faster inference speed. If you prioritize model storage size, choose a model with smaller storage size.</b>
<p><b>Layout Region Detection Module (Optional):</b></p>

* <b>Layout detection model, including 23 common categories: document title, paragraph title, text, page number, abstract, table of contents, references, footnotes, header, footer, algorithm, formula, formula number, image, chart title, table, table title, seal, chart title, chart, header image, footer image, sidebar text</b>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>mAP(0.5) (%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>PicoDet_layout_1x</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet_layout_1x_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet_layout_1x_pretrained.pdparams">Trained Model</a></td>
<td>86.8</td>
<td>9.03 / 3.10</td>
<td>25.82 / 20.70</td>
<td>7.4</td>
<td>An efficient layout area localization model trained on the PubLayNet dataset based on PicoDet-1x can locate five types of areas, including text, titles, tables, images, and lists.</td>
</tr>
<tr>
<td>PicoDet_layout_1x_table</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet_layout_1x_table_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet_layout_1x_table_pretrained.pdparams">Trained Model</a></td>
<td>95.7</td>
<td>8.02 / 3.09</td>
<td>23.70 / 20.41</td>
<td>7.4 M</td>
<td>An efficient layout area localization model trained on the PubLayNet dataset based on PicoDet-1x can locate one type of tables.</td>
</tr>
<tr>
<td>PicoDet-S_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-S_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-S_layout_3cls_pretrained.pdparams">Trained Model</a></td>
<td>87.1</td>
<td>8.99 / 2.22</td>
<td>16.11 / 8.73</td>
<td>4.8</td>
<td>An high-efficient layout area localization model trained on a self-constructed dataset based on PicoDet-S for scenarios such as Chinese and English papers, magazines, and research reports includes three categories: tables, images, and seals.</td>
</tr>
<tr>
<td>PicoDet-S_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-S_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-S_layout_17cls_pretrained.pdparams">Trained Model</a></td>
<td>70.3</td>
<td>9.11 / 2.12</td>
<td>15.42 / 9.12</td>
<td>4.8</td>
<td>A high-efficient layout area localization model trained on a self-constructed dataset based on PicoDet-S_layout_17cls for scenarios such as Chinese and English papers, magazines, and research reports includes 17 common layout categories, namely: paragraph titles, images, text, numbers, abstracts, content, chart titles, formulas, tables, table titles, references, document titles, footnotes, headers, algorithms, footers, and seals.</td>
</tr>
<tr>
<td>PicoDet-L_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-L_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-L_layout_3cls_pretrained.pdparams">Trained Model</a></td>
<td>89.3</td>
<td>13.05 / 4.50</td>
<td>41.30 / 41.30</td>
<td>22.6</td>
<td>An efficient layout area localization model trained on a self-constructed dataset based on PicoDet-L for scenarios such as Chinese and English papers, magazines, and research reports includes three categories: tables, images, and seals.</td>
</tr>
<tr>
<td>PicoDet-L_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-L_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-L_layout_17cls_pretrained.pdparams">Trained Model</a></td>
<td>79.9</td>
<td>13.50 / 4.69</td>
<td>43.32 / 43.32</td>
<td>22.6</td>
<td>A efficient layout area localization model trained on a self-constructed dataset based on PicoDet-L_layout_17cls for scenarios such as Chinese and English papers, magazines, and research reports includes 17 common layout categories, namely: paragraph titles, images, text, numbers, abstracts, content, chart titles, formulas, tables, table titles, references, document titles, footnotes, headers, algorithms, footers, and seals.</td>
</tr>
<tr>
<td>RT-DETR-H_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/RT-DETR-H_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/RT-DETR-H_layout_3cls_pretrained.pdparams">Trained Model</a></td>
<td>95.9</td>
<td>114.93 / 27.71</td>
<td>947.56 / 947.56</td>
<td>470.1</td>
<td>A high-precision layout area localization model trained on a self-constructed dataset based on RT-DETR-H for scenarios such as Chinese and English papers, magazines, and research reports includes three categories: tables, images, and seals.</td>
</tr>
<tr>
<td>RT-DETR-H_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/RT-DETR-H_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/RT-DETR-H_layout_17cls_pretrained.pdparams">Trained Model</a></td>
<td>92.6</td>
<td>115.29 / 104.09</td>
<td>995.27 / 995.27</td>
<td>470.2</td>
<td>A high-precision layout area localization model trained on a self-constructed dataset based on RT-DETR-H for scenarios such as Chinese and English papers, magazines, and research reports includes 17 common layout categories, namely: paragraph titles, images, text, numbers, abstracts, content, chart titles, formulas, tables, table titles, references, document titles, footnotes, headers, algorithms, footers, and seals.</td>
</tr>
</tbody>
</table>
<b>Note: The evaluation dataset for the above accuracy metrics is the self-built layout region detection dataset of PaddleOCR, which includes 500 common document images of Chinese and English papers, magazines, contracts, books, test papers, and research reports. GPU inference time is based on NVIDIA Tesla T4 machine, precision type is FP32, and CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz, with 8 threads, precision type is FP32.</b>

> ❗ The above listed are the <b>3 core models</b> that the layout detection module mainly supports. This module supports a total of <b>11 full models</b>, including multiple models predefined with different categories. Among them, there are 9 models that include the seal category. In addition to the above 3 core models, the remaining model list is as follows:

<details><summary> 👉Model List Details</summary>

* <b>3-category Layout Detection Models, including table, image, and seal</b>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>mAP(0.5) (%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
</thead>
<tbody>
<tr>
<td>PicoDet-S_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-S_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-S_layout_3cls_pretrained.pdparams">Training Model</a></td>
<td>88.2</td>
<td>8.99 / 2.22</td>
<td>16.11 / 8.73</td>
<td>4.8</td>
<td>A high-efficiency layout area localization model trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on the lightweight PicoDet-S model</td>
</tr>
<tr>
<td>PicoDet-L_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-L_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-L_layout_3cls_pretrained.pdparams">Training Model</a></td>
<td>89.0</td>
<td>13.05 / 4.50</td>
<td>41.30 / 41.30</td>
<td>22.6</td>
<td>A layout area localization model with balanced efficiency and accuracy, trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on PicoDet-L</td>
</tr>
<tr>
<td>RT-DETR-H_layout_3cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/RT-DETR-H_layout_3cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/RT-DETR-H_layout_3cls_pretrained.pdparams">Training Model</a></td>
<td>95.8</td>
<td>114.93 / 27.71</td>
<td>947.56 / 947.56</td>
<td>470.1</td>
<td>A high-precision layout area localization model trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on RT-DETR-H</td>
</tr>
</tbody></table>
<b>Note: The evaluation set for the above accuracy metrics is the layout area detection dataset self-built by PaddleOCR, which includes 1,154 images of common document types such as Chinese and English papers, magazines, and research reports. The GPU inference time is based on an NVIDIA Tesla T4 machine with FP32 precision. The CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>

* <b>17-category Layout Detection Models, including 17 common layout categories: paragraph title, image, text, number, abstract, content, figure title, formula, table, table title, reference, document title, footnote, header, algorithm, footer, seal</b>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>mAP(0.5) (%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
</thead>
<tbody>
<tr>
<td>PicoDet-S_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-S_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-S_layout_17cls_pretrained.pdparams">Training Model</a></td>
<td>87.4</td>
<td>9.11 / 2.12</td>
<td>15.42 / 9.12</td>
<td>4.8</td>
<td>A high-efficiency layout area localization model trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on the lightweight PicoDet-S model</td>
</tr>
<tr>
<td>PicoDet-L_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PicoDet-L_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PicoDet-L_layout_17cls_pretrained.pdparams">Training Model</a></td>
<td>89.0</td>
<td>13.50 / 4.69</td>
<td>43.32 / 43.32</td>
<td>22.6</td>
<td>A layout area localization model with balanced efficiency and accuracy, trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on PicoDet-L</td>
</tr>
<tr>
<td>RT-DETR-H_layout_17cls</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/RT-DETR-H_layout_17cls_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/RT-DETR-H_layout_17cls_pretrained.pdparams">Training Model</a></td>
<td>98.3</td>
<td>115.29 / 104.09</td>
<td>995.27 / 995.27</td>
<td>470.2</td>
<td>A high-precision layout area localization model trained on a self-built dataset for Chinese and English papers, magazines, and research reports based on RT-DETR-H</td>
</tr>
</tbody>
</table>
<b>Note: The evaluation set for the above accuracy metrics is the layout area detection dataset self-built by PaddleOCR, which includes 892 images of common document types such as Chinese and English papers, magazines, and research reports. The GPU inference time is based on an NVIDIA Tesla T4 machine with FP32 precision. The CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.</b>
</details>
<p><b>Document Image Orientation Classification Module (Optional):</b></p>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Top-1 Acc (%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>PP-LCNet_x1_0_doc_ori</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-LCNet_x1_0_doc_ori_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-LCNet_x1_0_doc_ori_pretrained.pdparams">Training Model</a></td>
<td>99.06</td>
<td>2.31 / 0.43</td>
<td>3.37 / 1.27</td>
<td>7</td>
<td>A document image classification model based on PP-LCNet_x1_0, containing four categories: 0 degrees, 90 degrees, 180 degrees, and 270 degrees</td>
</tr>
</tbody>
</table>
<p><b>Note: The above accuracy metrics are evaluated on a self-built dataset covering multiple scenarios such as certificates and documents, containing 1000 images. GPU inference time is based on NVIDIA Tesla T4 machine, precision type is FP32, CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz, with 8 threads, precision type is FP32.</b></p>
<p><b>Text Image Correction Module (Optional):</b></p>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>CER</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>UVDoc</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/UVDoc_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/UVDoc_pretrained.pdparams">Training Model</a></td>
<td>0.179</td>
<td>30.3 M</td>
<td>High-precision text image correction model</td>
</tr>
</tbody>
</table>
<b>Note: The accuracy metrics of the model are measured from the <a href="https://www3.cs.stonybrook.edu/~cvl/docunet.html">DocUNet benchmark</a>.</b>
<p><b>Text Detection Module:</b></p>
<table>
<thead>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Detection Hmean (%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>PP-OCRv4_server_seal_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_server_seal_det_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_server_seal_det_pretrained.pdparams">Trained Model</a></td>
<td>98.21</td>
<td>74.75 / 67.72</td>
<td>382.55 / 382.55</td>
<td>109</td>
<td>PP-OCRv4 server-side seal text detection model, with higher accuracy, suitable for deployment on better servers</td>
</tr>
<tr>
<td>PP-OCRv4_mobile_seal_det</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_mobile_seal_det_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_mobile_seal_det_pretrained.pdparams">Trained Model</a></td>
<td>96.47</td>
<td>7.82 / 3.09</td>
<td>48.28 / 23.97</td>
<td>4.6</td>
<td>PP-OCRv4 mobile-side seal text detection model, with higher efficiency, suitable for deployment on the edge</td>
</tr>
</tbody>
</table>
<b>Note: The above accuracy metrics are evaluated on a self-built dataset containing 500 circular seal images. GPU inference time is based on NVIDIA Tesla T4 machine, precision type is FP32, CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz, with 8 threads, precision type is FP32.</b>
<p><b>Text Recognition Module:</b></p>
<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Recognition Avg Accuracy(%)</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>CPU Inference Time (ms)<br/>[Normal Mode / High-Performance Mode]</th>
<th>Model Storage Size (M)</th>
<th>Description</th>
</tr>
<tr>
<td>PP-OCRv4_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_mobile_rec_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_mobile_rec_pretrained.pdparams">Trained Model</a></td>
<td>78.20</td>
<td>4.82 / 4.82</td>
<td>16.74 / 4.64</td>
<td>10.6 M</td>
<td>The PP-OCRv4 recognition model is an upgrade from PP-OCRv3. Under comparable speed conditions, the effect in Chinese and English scenarios is further improved. The average recognition accuracy of the 80 multilingual models is increased by more than 8%.</td>
</tr>
<tr>
<td>PP-OCRv4_server_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv4_server_rec_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv4_server_rec_pretrained.pdparams">Trained Model</a></td>
<td>79.20</td>
<td>6.58 / 6.58</td>
<td>33.17 / 33.17</td>
<td>71.2 M</td>
<td>A high-precision server text recognition model, featuring high accuracy, fast speed, and multilingual support. It is suitable for text recognition tasks in various scenarios.</td>
</tr>
<tr>
<td>PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td>5.87 / 5.87</td>
<td>9.07 / 4.28</td>
<td></td>
<td>An ultra-lightweight OCR model suitable for mobile applications. It adopts an encoder-decoder structure based on Transformer and enhances recognition accuracy and efficiency through techniques such as data augmentation and mixed precision training. The model size is 10.6M, making it suitable for deployment on resource-constrained devices. It can be used in scenarios such as mobile photo translation and business card recognition.</td>
</tr>
</table>
<p><b>Note: The evaluation set for the above accuracy indicators is the Chinese dataset built by PaddleOCR, covering multiple scenarios such as street view, web images, documents, and handwriting. The text recognition includes 11,000 images. The GPU inference time for all models is based on NVIDIA Tesla T4 machines with FP32 precision type. The CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision type.</b></p>
<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Recognition Avg Accuracy(%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
<tr>
<td>ch_SVTRv2_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/ch_SVTRv2_rec_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/ch_SVTRv2_rec_pretrained.pdparams">Training Model</a></td>
<td>68.81</td>
<td>8.36801</td>
<td>165.706</td>
<td>73.9 M</td>
<td rowspan="1">
SVTRv2 is a server text recognition model developed by the OpenOCR team of Fudan University's Visual and Learning Laboratory (FVL). It won the first prize in the PaddleOCR Algorithm Model Challenge - Task One: OCR End-to-End Recognition Task. The end-to-end recognition accuracy on the A list is 6% higher than that of PP-OCRv4.
</td>
</tr>
</table>
<p><b>Note: The evaluation set for the above accuracy indicators is the <a href="https://aistudio.baidu.com/competition/detail/1131/0/introduction">PaddleOCR Algorithm Model Challenge</a> - Task One: OCR End-to-End Recognition Task A list. The GPU inference time for all models is based on NVIDIA Tesla T4 machines with FP32 precision type. The CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision type.</b></p>
<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Recognition Avg Accuracy(%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
<tr>
<td>ch_RepSVTR_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/ch_RepSVTR_rec_infer.tar">Inference Model</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/ch_RepSVTR_rec_pretrained.pdparams">Training Model</a></td>
<td>65.07</td>
<td>10.5047</td>
<td>51.5647</td>
<td>22.1 M</td>
<td rowspan="1">    The RepSVTR text recognition model is a mobile text recognition model based on SVTRv2. It won the first prize in the PaddleOCR Algorithm Model Challenge - Task One: OCR End-to-End Recognition Task. The end-to-end recognition accuracy on the B list is 2.5% higher than that of PP-OCRv4, with the same inference speed.</td>
</tr>
</table>
<p><b>Note: The evaluation set for the above accuracy indicators is the <a href="https://aistudio.baidu.com/competition/detail/1131/0/introduction">PaddleOCR Algorithm Model Challenge</a> - Task One: OCR End-to-End Recognition Task B list. The GPU inference time for all models is based on NVIDIA Tesla T4 machines with FP32 precision type. The CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision type.</b></p>

* <b>English Recognition Model</b>
<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Recognition Avg Accuracy(%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
<tr>
<td>en_PP-OCRv4_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/en_PP-OCRv4_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>[Latest] Further upgraded based on PP-OCRv3, with improved accuracy under comparable speed conditions.</td>
</tr>
<tr>
<td>en_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/en_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Ultra-lightweight model, supporting English and numeric recognition.</td>
</tr>
</table>

* <b>Multilingual Recognition Model</b>
<table>
<tr>
<th>Model</th><th>Model Download Link</th>
<th>Recognition Avg Accuracy(%)</th>
<th>GPU Inference Time (ms)</th>
<th>CPU Inference Time</th>
<th>Model Storage Size (M)</th>
<th>Introduction</th>
</tr>
<tr>
<td>korean_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/korean_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Korean Recognition</td>
</tr>
<tr>
<td>japan_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/japan_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Japanese Recognition</td>
</tr>
<tr>
<td>chinese_cht_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/chinese_cht_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Traditional Chinese Recognition</td>
</tr>
<tr>
<td>te_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/te_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Telugu Recognition</td>
</tr>
<tr>
<td>ka_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/ka_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Kannada Recognition</td>
</tr>
<tr>
<td>ta_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/ta_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Tamil Recognition</td>
</tr>
<tr>
<td>latin_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/latin_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Latin Recognition</td>
</tr>
<tr>
<td>arabic_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/arabic_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Arabic Script Recognition</td>
</tr>
<tr>
<td>cyrillic_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/cyrillic_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Cyrillic Script Recognition</td>
</tr>
<tr>
<td>devanagari_PP-OCRv3_mobile_rec</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0rc0/devanagari_PP-OCRv3_mobile_rec_infer.tar">Inference Model</a>/<a href="">Training Model</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Devanagari Script Recognition</td>
</tr>
</table>


## 2. Quick Start
The pre-trained model pipelines provided by PaddleX can be quickly experienced. You can experience the seal text recognition pipeline locally using the command line or Python.

Before using the seal text recognition pipeline locally, please ensure that you have completed the installation of the PaddleX wheel package according to the [PaddleX Local Installation Tutorial](../../../installation/installation.en.md).

### 2.1 Command Line Experience
You can quickly experience the seal text recognition pipeline with a single command. Use the [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png), and replace `--input` with the local path for prediction.

```bash
paddlex --pipeline seal_recognition \
    --input seal_text_det.png \
    --use_doc_orientation_classify False \
    --use_doc_unwarping False \
    --device gpu:0 \
    --save_path ./output
```

The relevant parameter descriptions can be referred to in the parameter explanations of [2.1.2 Integration via Python Script](#212-integration-via-python-script).

After running, the results will be printed to the terminal, as follows:

<details><summary> 👉Click to Expand</summary>

```bash
{'res': {'input_path': 'seal_text_det.png', 'model_settings': {'use_doc_preprocessor': False, 'use_layout_detection': True}, 'layout_det_res': {'input_path': None, 'page_index': None, 'boxes': [{'cls_id': 16, 'label': 'seal', 'score': 0.975529670715332, 'coordinate': [6.191284, 0.16680908, 634.39325, 628.85345]}]}, 'seal_res_list': [{'input_path': None, 'page_index': None, 'model_settings': {'use_doc_preprocessor': False, 'use_textline_orientation': False}, 'dt_polys': [array([[320,  38],
       [479,  92],
       [483,  94],
       [486,  97],
       [579, 226],
       [582, 230],
       [582, 235],
       [584, 383],
       [584, 388],
       [582, 392],
       [578, 396],
       [573, 398],
       [566, 398],
       [502, 380],
       [497, 377],
       [494, 374],
       [491, 369],
       [491, 366],
       [488, 259],
       [424, 172],
       [318, 136],
       [251, 154],
       [200, 174],
       [137, 260],
       [133, 366],
       [132, 370],
       [130, 375],
       [126, 378],
       [123, 380],
       [ 60, 398],
       [ 55, 398],
       [ 49, 397],
       [ 45, 394],
       [ 43, 390],
       [ 41, 383],
       [ 43, 236],
       [ 44, 230],
       [ 45, 227],
       [141,  96],
       [144,  93],
       [148,  90],
       [311,  38],
       [315,  38]]), array([[461, 347],
       [465, 350],
       [468, 354],
       [470, 360],
       [470, 425],
       [469, 429],
       [467, 433],
       [462, 437],
       [456, 439],
       [169, 439],
       [165, 439],
       [160, 436],
       [157, 432],
       [155, 426],
       [154, 360],
       [155, 356],
       [158, 352],
       [161, 348],
       [168, 346],
       [456, 346]]), array([[439, 445],
       [441, 447],
       [443, 451],
       [444, 453],
       [444, 497],
       [443, 502],
       [440, 504],
       [437, 506],
       [434, 507],
       [189, 505],
       [184, 504],
       [182, 502],
       [180, 498],
       [179, 496],
       [181, 453],
       [182, 449],
       [184, 446],
       [188, 444],
       [434, 444]]), array([[158, 468],
       [199, 502],
       [242, 522],
       [299, 534],
       [339, 532],
       [373, 526],
       [417, 508],
       [459, 475],
       [462, 474],
       [467, 474],
       [472, 476],
       [502, 507],
       [503, 510],
       [504, 515],
       [503, 518],
       [501, 521],
       [452, 559],
       [450, 560],
       [391, 584],
       [390, 584],
       [372, 590],
       [370, 590],
       [305, 596],
       [302, 596],
       [224, 581],
       [221, 580],
       [164, 553],
       [162, 551],
       [114, 509],
       [112, 507],
       [111, 503],
       [112, 498],
       [114, 496],
       [146, 468],
       [149, 466],
       [154, 466]])], 'text_det_params': {'limit_side_len': 736, 'limit_type': 'min', 'thresh': 0.2, 'box_thresh': 0.6, 'unclip_ratio': 0.5}, 'text_type': 'seal', 'textline_orientation_angles': [-1, -1, -1, -1], 'text_rec_score_thresh': 0, 'rec_texts': ['天津君和缘商贸有限公司', '发票专用章', '吗繁物', '5263647368706'], 'rec_scores': [0.9934046268463135, 0.9999403953552246, 0.998250424861908, 0.9913849234580994], 'rec_polys': [array([[320,  38],
       [479,  92],
       [483,  94],
       [486,  97],
       [579, 226],
       [582, 230],
       [582, 235],
       [584, 383],
       [584, 388],
       [582, 392],
       [578, 396],
       [573, 398],
       [566, 398],
       [502, 380],
       [497, 377],
       [494, 374],
       [491, 369],
       [491, 366],
       [488, 259],
       [424, 172],
       [318, 136],
       [251, 154],
       [200, 174],
       [137, 260],
       [133, 366],
       [132, 370],
       [130, 375],
       [126, 378],
       [123, 380],
       [ 60, 398],
       [ 55, 398],
       [ 49, 397],
       [ 45, 394],
       [ 43, 390],
       [ 41, 383],
       [ 43, 236],
       [ 44, 230],
       [ 45, 227],
       [141,  96],
       [144,  93],
       [148,  90],
       [311,  38],
       [315,  38]]), array([[461, 347],
       [465, 350],
       [468, 354],
       [470, 360],
       [470, 425],
       [469, 429],
       [467, 433],
       [462, 437],
       [456, 439],
       [169, 439],
       [165, 439],
       [160, 436],
       [157, 432],
       [155, 426],
       [154, 360],
       [155, 356],
       [158, 352],
       [161, 348],
       [168, 346],
       [456, 346]]), array([[439, 445],
       [441, 447],
       [443, 451],
       [444, 453],
       [444, 497],
       [443, 502],
       [440, 504],
       [437, 506],
       [434, 507],
       [189, 505],
       [184, 504],
       [182, 502],
       [180, 498],
       [179, 496],
       [181, 453],
       [182, 449],
       [184, 446],
       [188, 444],
       [434, 444]]), array([[158, 468],
       [199, 502],
       [242, 522],
       [299, 534],
       [339, 532],
       [373, 526],
       [417, 508],
       [459, 475],
       [462, 474],
       [467, 474],
       [472, 476],
       [502, 507],
       [503, 510],
       [504, 515],
       [503, 518],
       [501, 521],
       [452, 559],
       [450, 560],
       [391, 584],
       [390, 584],
       [372, 590],
       [370, 590],
       [305, 596],
       [302, 596],
       [224, 581],
       [221, 580],
       [164, 553],
       [162, 551],
       [114, 509],
       [112, 507],
       [111, 503],
       [112, 498],
       [114, 496],
       [146, 468],
       [149, 466],
       [154, 466]])], 'rec_boxes': array([], dtype=float64)}]}}
```

</details>

The explanation of the result parameters can be found in [2.1.2 Python Script Integration](#212-python-script-integration).

The visualized results are saved under `save_path`, and the visualized result of seal OCR is as follows:

<img src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/seal_recognition/03.png"/>

### 2.1.2 Python Script Integration

* The above command line is for quickly experiencing and viewing the effect. Generally, in a project, you often need to integrate through code. You can complete the quick inference of the pipeline with just a few lines of code. The inference code is as follows:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="seal_recognition")

output = pipeline.predict(
    "seal_text_det.png",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
)
for res in output:
    res.print() 
    res.save_to_img("./output/") 
    res.save_to_json("./output/") 
```

In the above Python script, the following steps were executed:

(1) The seal recognition production line object was instantiated via `create_pipeline()`, with the specific parameters described as follows:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Type</th>
<th>Default Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pipeline</code></td>
<td>The name of the production line or the path to the production line configuration file. If it is a production line name, it must be supported by PaddleX.</td>
<td><code>str</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>config</code></td>
<td>Specific configuration information for the production line (if set simultaneously with <code>pipeline</code>, it has higher priority than <code>pipeline</code>, and the production line name must be consistent with <code>pipeline</code>).</td>
<td><code>dict[str, Any]</code></td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>The device used for production line inference. It supports specifying the specific card number of the GPU, such as "gpu:0", other hardware card numbers, such as "npu:0", or CPU, such as "cpu".</td>
<td><code>str</code></td>
<td><code>gpu:0</code></td>
</tr>
<tr>
<td><code>use_hpip</code></td>
<td>Whether to enable high-performance inference. This is only available if the production line supports high-performance inference.</td>
<td><code>bool</code></td>
<td><code>False</code></td>
</tr>
</tbody>
</table>

(2) Call the `predict()` method of the Seal Text Recognition pipeline object for inference prediction. This method will return a `generator`. Below are the parameters and their descriptions for the `predict()` method:

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Type</th>
<th>Options</th>
<th>Default Value</th>
</tr>
</thead>
<tr>
<td><code>input</code></td>
<td>Data to be predicted, supports multiple input types (required)</td>
<td><code>Python Var|str|list</code></td>
<td>
<ul>
<li><b>Python Var</b>: Image data represented by <code>numpy.ndarray</code></li>
<li><b>str</b>: Local path of an image or PDF file, e.g., <code>/root/data/img.jpg</code>; <b>URL link</b>, e.g., the network URL of an image or PDF file: <a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png">Example</a>; <b>Local directory</b>, containing images to be predicted, e.g., <code>/root/data/</code> (currently does not support prediction of PDF files in directories; PDF files must be specified with an exact file path)</li>
<li><b>List</b>: Elements of the list must be of the above types, e.g., <code>[numpy.ndarray, numpy.ndarray]</code>, <code>[\"/root/data/img1.jpg\", \"/root/data/img2.jpg\"]</code>, <code>[\"/root/data1\", \"/root/data2\"]</code></li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>device</code></td>
<td>Inference device for the pipeline</td>
<td><code>str|None</code></td>
<td>
<ul>
<li><b>CPU</b>: e.g., <code>cpu</code> for CPU inference;</li>
<li><b>GPU</b>: e.g., <code>gpu:0</code> for inference using the first GPU;</li>
<li><b>NPU</b>: e.g., <code>npu:0</code> for inference using the first NPU;</li>
<li><b>XPU</b>: e.g., <code>xpu:0</code> for inference using the first XPU;</li>
<li><b>MLU</b>: e.g., <code>mlu:0</code> for inference using the first MLU;</li>
<li><b>DCU</b>: e.g., <code>dcu:0</code> for inference using the first DCU;</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used. During initialization, the local GPU device 0 will be prioritized; if unavailable, the CPU device will be used.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>use_doc_orientation_classify</code></td>
<td>Whether to use the document orientation classification module</td>
<td><code>bool|None</code></td>
<td>
<ul>
<li><b>bool</b>: <code>True</code> or <code>False</code>;</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>True</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>use_doc_unwarping</code></td>
<td>Whether to use the document unwarping module</td>
<td><code>bool|None</code></td>
<td>
<ul>
<li><b>bool</b>: <code>True</code> or <code>False</code>;</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>True</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>use_layout_detection</code></td>
<td>Whether to use the layout detection module</td>
<td><code>bool|None</code></td>
<td>
<ul>
<li><b>bool</b>: <code>True</code> or <code>False</code>;</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>True</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>layout_threshold</code></td>
<td>Confidence threshold for layout detection; only scores above this threshold will be output</td>
<td><code>float|dict|None</code></td>
<td>
<ul>
<li><b>float</b>: Any float greater than <code>0</code></li>
<li><b>dict</b>: Key is the int category ID, value is any float greater than <code>0</code></li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>0.5</code></li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>layout_nms</code></td>
<td>Whether to use Non-Maximum Suppression (NMS) for layout detection post-processing</td>
<td><code>bool|None</code></td>
<td>
<ul>
<li><b>bool</b>: <code>True</code> or <code>False</code>;</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>True</code>.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>layout_unclip_ratio</code></td>
<td>Expansion ratio of detection box edges; if not specified, the default value from the PaddleX official model configuration will be used</td>
<td><code>float|list|None</code></td>
<td>
<ul>
<li><b>float</b>: Any float greater than 0, e.g., 1.1, which means expanding the width and height of the detection box by 1.1 times while keeping the center unchanged</li>
<li><b>list</b>: e.g., [1.2, 1.5], which means expanding the width of the detection box by 1.2 times and the height by 1.5 times while keeping the center unchanged</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as 1.0</li>
</ul>
</td>
</tr>
<tr>
<td><code>layout_merge_bboxes_mode</code></td>
<td>Merging mode for detection boxes in layout detection output; if not specified, the default value from the PaddleX official model configuration will be used</td>
<td><code>string|None</code></td>
<td>
<ul>
<li><b>large</b>: When set to <code>large</code>, only the largest external box will be retained for overlapping detection boxes, and the internal overlapping boxes will be removed.</li>
<li><b>small</b>: When set to <code>small</code>, only the smallest internal box will be retained for overlapping detection boxes, and the external overlapping boxes will be removed.</li>
<li><b>union</b>: No filtering of boxes will be performed; both internal and external boxes will be retained.</li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>large</code>.</li>
</ul>
</td>
<td>None</td>
</tr>
<tr>
<td><code>seal_det_limit_side_len</code></td>
<td>Side length limit for seal text detection</td>
<td><code>int|None</code></td>
<td>
<ul>
<li><b>int</b>: Any integer greater than <code>0</code></li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>736</code></li>
</ul>
</td>
<td><code>None</code></td>
</tr>
<tr>
<td><code>seal_rec_score_thresh</code></td>
<td>Text recognition threshold; text results with scores above this threshold will be retained</td>
<td><code>float|None</code></td>
<td>
<ul>
<li><b>float</b>: Any float greater than <code>0</code></li>
<li><b>None</b>: If set to <code>None</code>, the default value from the pipeline initialization will be used, initialized as <code>0.0</code>. This means no threshold is applied.</li>
</ul>
</td>
<td><code>None</code></td>
</tr>
</table>

(3) Process the prediction results. The prediction result for each sample is of `dict` type and supports operations such as printing, saving as an image, and saving as a `json` file:

<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
<th>Parameter</th>
<th>Parameter Type</th>
<th>Parameter Description</th>
<th>Default Value</th>
</tr>
</thead>
<tr>
<td rowspan="3"><code>print()</code></td>
<td rowspan="3">Print results to the terminal</td>
<td><code>format_json</code></td>
<td><code>bool</code></td>
<td>Whether to format the output content using <code>JSON</code> indentation</td>
<td><code>True</code></td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>Specify the indentation level to beautify the output <code>JSON</code> data for better readability, effective only when <code>format_json</code> is <code>True</code></td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>Control whether to escape non-<code>ASCII</code> characters to <code>Unicode</code>. When set to <code>True</code>, all non-<code>ASCII</code> characters will be escaped; <code>False</code> will retain the original characters, effective only when <code>format_json</code> is <code>True</code></td>
<td><code>False</code></td>
</tr>
<tr>
<td rowspan="3"><code>save_to_json()</code></td>
<td rowspan="3">Save results as a json file</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>The file path to save the results. When it is a directory, the saved file name will be consistent with the input file type</td>
<td>None</td>
</tr>
<tr>
<td><code>indent</code></td>
<td><code>int</code></td>
<td>Specify the indentation level to beautify the output <code>JSON</code> data for better readability, effective only when <code>format_json</code> is <code>True</code></td>
<td>4</td>
</tr>
<tr>
<td><code>ensure_ascii</code></td>
<td><code>bool</code></td>
<td>Control whether to escape non-<code>ASCII</code> characters to <code>Unicode</code>. When set to <code>True</code>, all non-<code>ASCII</code> characters will be escaped; <code>False</code> will retain the original characters, effective only when <code>format_json</code> is <code>True</code></td>
<td><code>False</code></td>
</tr>
<tr>
<td><code>save_to_img()</code></td>
<td>Save results as an image file</td>
<td><code>save_path</code></td>
<td><code>str</code></td>
<td>The file path to save the results, supports directory or file path</td>
<td>None</td>
</tr>
</table>

- Calling the `print()` method will print the results to the terminal, and the explanations of the printed content are as follows:

    - `input_path`: `(str)` The input path of the image to be predicted.

    - `model_settings`: `(Dict[str, bool])` The model parameters required for pipeline configuration.

        - `use_doc_preprocessor`: `(bool)` Controls whether to enable the document preprocessing sub-pipeline.
        - `use_layout_detection`: `(bool)` Controls whether to enable the layout detection sub-module.

    - `layout_det_res`: `(Dict[str, Union[List[numpy.ndarray], List[float]]])` The output result of the layout detection sub-module. Only exists when `use_layout_detection=True`.

        - `input_path`: `(Union[str, None])` The image path accepted by the layout detection module. Saved as `None` when the input is a `numpy.ndarray`.
        - `page_index`: `(Union[int, None])` Indicates the current page number of the PDF if the input is a PDF file; otherwise, it is `None`.
        - `boxes`: `(List[Dict])` A list of detected layout seal regions, with each element containing the following fields:
            - `cls_id`: `(int)` The class ID of the detected seal region.
            - `score`: `(float)` The confidence score of the detected region.
            - `coordinate`: `(List[float])` The coordinates of the four corners of the detection box, in the order of x1, y1, x2, y2, representing the x-coordinate of the top-left corner, the y-coordinate of the top-left corner, the x-coordinate of the bottom-right corner, and the y-coordinate of the bottom-right corner.

    - `seal_res_list`: `List[Dict]` A list of seal text recognition results, with each element containing the following fields:

        - `input_path`: `(Union[str, None])` The image path accepted by the seal text recognition pipeline. Saved as `None` when the input is a `numpy.ndarray`.
        - `page_index`: `(Union[int, None])` Indicates the current page number of the PDF if the input is a PDF file; otherwise, it is `None`.
        - `model_settings`: `(Dict[str, bool])` The model configuration parameters for the seal text recognition pipeline.
          - `use_doc_preprocessor`: `(bool)` Controls whether to enable the document preprocessing sub-pipeline.
          - `use_textline_orientation`: `(bool)` Controls whether to enable the text line orientation classification sub-module.

    - `doc_preprocessor_res`: `(Dict[str, Union[str, Dict[str, bool], int]])` The output result of the document preprocessing sub-pipeline. Only exists when `use_doc_preprocessor=True`.

        - `input_path`: `(Union[str, None])` The image path accepted by the document preprocessing sub-pipeline. Saved as `None` when the input is a `numpy.ndarray`.
        - `model_settings`: `(Dict)` The model configuration parameters for the preprocessing sub-pipeline.
            - `use_doc_orientation_classify`: `(bool)` Controls whether to enable document orientation classification.
            - `use_doc_unwarping`: `(bool)` Controls whether to enable document unwarping.
        - `angle`: `(int)` The predicted result of document orientation classification. When enabled, it takes values [0, 1, 2, 3], corresponding to [0°, 90°, 180°, 270°]; when disabled, it is -1.

    - `dt_polys`: `(List[numpy.ndarray])` A list of polygon boxes for seal text detection. Each detection box is represented by a numpy array of multiple vertex coordinates, with the array shape being (n, 2).

    - `dt_scores`: `(List[float])` A list of confidence scores for text detection boxes.

    - `text_det_params`: `(Dict[str, Dict[str, int, float]])` Configuration parameters for the text detection module.
        - `limit_side_len`: `(int)` The side length limit value during image preprocessing.
        - `limit_type`: `(str)` The handling method for side length limits.
        - `thresh`: `(float)` The confidence threshold for text pixel classification.
        - `box_thresh`: `(float)` The confidence threshold for text detection boxes.
        - `unclip_ratio`: `(float)` The expansion ratio for text detection boxes.
        - `text_type`: `(str)` The type of seal text detection, currently fixed as "seal".

    - `text_rec_score_thresh`: `(float)` The filtering threshold for text recognition results.

    - `rec_texts`: `(List[str])` A list of text recognition results, containing only texts with confidence scores above `text_rec_score_thresh`.

    - `rec_scores`: `(List[float])` A list of confidence scores for text recognition, filtered by `text_rec_score_thresh`.

    - `rec_polys`: `(List[numpy.ndarray])` A list of text detection boxes filtered by confidence score, in the same format as `dt_polys`.

    - `rec_boxes`: `(numpy.ndarray)` An array of rectangular bounding boxes for detection boxes; the seal recognition pipeline returns an empty array.

- Calling the `save_to_json()` method will save the above content to the specified `save_path`. If a directory is specified, the saved path will be `save_path/{your_img_basename}_res.json`. If a file is specified, it will be saved directly to that file. Since JSON files do not support saving numpy arrays, `numpy.array` types will be converted to list format.

- Calling the `save_to_img()` method will save the visualization results to the specified `save_path`. If a directory is specified, the saved path will be `save_path/{your_img_basename}_seal_res_region1.{your_img_extension}`. If a file is specified, it will be saved directly to that file. (The pipeline usually contains multiple result images, so it is not recommended to specify a specific file path directly, as multiple images will be overwritten, and only the last image will be retained.)

* Additionally, you can obtain visualized images with results and prediction results through attributes, as follows:

<table>
<thead>
<tr>
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tr>
<td rowspan="1"><code>json</code></td>
<td rowspan="1">Get the prediction results in <code>json</code> format.</td>
</tr>
<tr>
<td rowspan="2"><code>img</code></td>
<td rowspan="2">Get the visualization results in <code>dict</code> format.</td>
</tr>
</table>

- The prediction results obtained through the `json` attribute are of dict type, with content consistent with what is saved by calling the `save_to_json()` method.
- The prediction results returned by the `img` attribute are of dict type. The keys are `layout_det_res`, `seal_res_region1`, and `preprocessed_img`, corresponding to three `Image.Image` objects: one for visualizing layout detection, one for visualizing seal text recognition results, and one for visualizing image preprocessing. If the image preprocessing sub-module is not used, `preprocessed_img` will not be included in the dictionary. If the layout region detection module is not used, `layout_det_res` will not be included.

Additionally, you can obtain the configuration file for the seal text recognition pipeline and load the configuration file for prediction. You can execute the following command to save the results in `my_path`:

```
paddlex --get_pipeline_config seal_recognition --save_path ./my_path
```

If you have obtained the configuration file, you can customize the settings for the seal text recognition production line by simply modifying the `pipeline` parameter value in the `create_pipeline` method to the path of the production line configuration file. The example is as follows:

```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/seal_recognition.yaml")
output = pipeline.predict("seal_text_det.png")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_img("./output/") ## 保存可视化结果
    res.save_to_json("./output/") ## 保存预测结果的json文件
```

<b>Note:</b> The parameters in the configuration file are the pipeline initialization parameters. If you wish to change the initialization parameters of the seal text recognition pipeline, you can directly modify the parameters in the configuration file and load the configuration file for prediction. Additionally, CLI prediction also supports passing in a configuration file. Simply specify the path of the configuration file with `--pipeline`.

## 3. Development Integration/Deployment
If the pipeline meets your requirements for inference speed and accuracy, you can proceed directly with development integration/deployment.

If you need to integrate the pipeline into your Python project, you can refer to the example code in [2.2.2 Python Script Method](#222-python脚本方式集成).

In addition, PaddleX also provides three other deployment methods, which are detailed as follows:

🚀 <b>High-Performance Deployment</b>: In practical production environments, many applications have strict performance requirements (especially response speed) for deployment strategies to ensure efficient system operation and smooth user experience. To this end, PaddleX provides a high-performance inference plugin that aims to deeply optimize the performance of model inference and pre/post-processing, significantly speeding up the end-to-end process. For detailed high-performance deployment procedures, please refer to the [PaddleX High-Performance Deployment Guide](../../../pipeline_deploy/high_performance_inference.en.md).

☁️ <b>Service-Oriented Deployment</b>: Service-oriented deployment is a common form of deployment in practical production environments. By encapsulating inference capabilities as services, clients can access these services via network requests to obtain inference results. PaddleX supports various pipeline service-oriented deployment solutions. For detailed pipeline service-oriented deployment procedures, please refer to the [PaddleX Service-Oriented Deployment Guide](../../../pipeline_deploy/serving.en.md).

Below are the API references for basic service-oriented deployment and multi-language service invocation examples:

<details><summary>API Reference</summary>
<p>For the main operations provided by the service:</p>
<ul>
<li>The HTTP request method is POST.</li>
<li>Both the request body and response body are JSON data (JSON objects).</li>
<li>When the request is processed successfully, the response status code is <code>200</code>, and the response body has the following properties:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>The UUID of the request.</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Fixed to <code>0</code>.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error message. Fixed to <code>"Success"</code>.</td>
</tr>
<tr>
<td><code>result</code></td>
<td><code>object</code></td>
<td>Operation result.</td>
</tr>
</tbody>
</table>
<ul>
<li>When the request is not processed successfully, the response body has the following properties:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>logId</code></td>
<td><code>string</code></td>
<td>The UUID of the request.</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>integer</code></td>
<td>Error code. Same as the response status code.</td>
</tr>
<tr>
<td><code>errorMsg</code></td>
<td><code>string</code></td>
<td>Error message.</td>
</tr>
</tbody>
</table>
<p>The main operations provided by the service are as follows:</p>
<ul>
<li><b><code>infer</code></b></li>
</ul>
<p>Get seal text recognition results.</p>
<p><code>POST /seal-recognition</code></p>
<ul>
<li>The request body has the following properties:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>file</code></td>
<td><code>string</code></td>
<td>The URL of an image or PDF file accessible to the server, or the Base64 encoded result of the content of the above file types. For PDF files exceeding 10 pages, only the content of the first 10 pages will be used.</td>
<td>Yes</td>
</tr>
<tr>
<td><code>fileType</code></td>
<td><code>integer</code></td>
<td>File type. <code>0</code> indicates a PDF file, <code>1</code> indicates an image file. If this property is not present in the request body, the file type will be inferred from the URL.</td>
<td>No</td>
</tr>
</tbody>
</table>
<ul>
<li>When the request is processed successfully, the <code>result</code> property of the response body has the following properties:</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sealRecResults</code></td>
<td><code>object</code></td>
<td>Seal text recognition results. The array length is 1 (for image input) or the smaller of the document page count and 10 (for PDF input). For PDF input, each element in the array represents the processing result of each page in the PDF file in order.</td>
</tr>
<tr>
<td><code>dataInfo</code></td>
<td><code>object</code></td>
<td>Input data information.</td>
</tr>
</tbody>
</table>
<p>Each element in <code>sealRecResults</code> is an <code>object</code> with the following properties:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>texts</code></td>
<td><code>array</code></td>
<td>Text position, content, and score.</td>
</tr>
<tr>
<td><code>inputImage</code></td>
<td><code>string</code></td>
<td>Input image. The image is in JPEG format and encoded using Base64.</td>
</tr>
<tr>
<td><code>layoutImage</code></td>
<td><code>string</code></td>
<td>Layout area detection result image. The image is in JPEG format and encoded using Base64.</td>
</tr>
<tr>
<td><code>ocrImage</code></td>
<td><code>string</code></td>
<td>OCR result image. The image is in JPEG format and encoded using Base64.</td>
</tr>
</tbody>
</table>
<p>Each element in <code>texts</code> is an <code>object</code> with the following properties:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>poly</code></td>
<td><code>array</code></td>
<td>Text position. The elements in the array are the vertex coordinates of the polygon surrounding the text.</td>
</tr>
<tr>
<td><code>text</code></td>
<td><code>string</code></td>
<td>Text content.</td>
</tr>
<tr>
<td><code>score</code></td>
<td><code>number</code></td>
<td>Text recognition score.</td>
</tr>
</tbody>
</table></details>
<details><summary>Multi-language Service Call Examples</summary>
<details>
<summary>Python</summary>
<pre><code class="language-python">import base64
import requests

API_URL = "http://localhost:8080/seal-recognition"
file_path = "./demo.jpg"

with open(file_path, "rb") as file:
    file_bytes = file.read()
    file_data = base64.b64encode(file_bytes).decode("ascii")

payload = {"file": file_data, "fileType": 1}

response = requests.post(API_URL, json=payload)

assert response.status_code == 200
result = response.json()["result"]
for i, res in enumerate(result["sealRecResults"]):
    print("Detected texts:")
    print(res["texts"])
    layout_img_path = f"layout_{i}.jpg"
    with open(layout_img_path, "wb") as f:
        f.write(base64.b64decode(res["layoutImage"]))
    ocr_img_path = f"ocr_{i}.jpg"
    with open(ocr_img_path, "wb") as f:
        f.write(base64.b64decode(res["ocrImage"]))
    print(f"Output images saved at {layout_img_path} and {ocr_img_path}")
</code></pre></details>
</details>
<br/>

📱 <b>Edge Deployment</b>: Edge deployment is a method of placing computing and data processing capabilities directly on user devices, allowing devices to process data without relying on remote servers. PaddleX supports deploying models on edge devices such as Android. For detailed edge deployment procedures, please refer to the [PaddleX Edge Deployment Guide](../../../pipeline_deploy/edge_deploy.en.md).
You can choose the appropriate deployment method based on your needs to integrate the model pipeline into subsequent AI applications.

## 4. Custom Development
If the default model weights provided by the seal text recognition pipeline do not meet your requirements in terms of accuracy or speed, you can try to <b>fine-tune</b> the existing models using <b>your own domain-specific or application data</b> to improve the recognition performance of the seal text recognition pipeline in your scenario.

### 4.1 Model Fine-Tuning
Since the seal text recognition pipeline consists of several modules, if the pipeline's performance does not meet expectations, the issue may arise from any one of these modules. You can analyze images with poor recognition results to identify which module is problematic and refer to the corresponding fine-tuning tutorial links in the table below for model fine-tuning.

<table>
<thead>
<tr>
<th>Scenario</th>
<th>Fine-Tuning Module</th>
<th>Fine-Tuning Reference Link</th>
</tr>
</thead>
<tbody>
<tr>
<td>Inaccurate or missing seal position detection</td>
<td>Layout Detection Module</td>
<td><a href="../../../module_usage/tutorials/ocr_modules/layout_detection.en.md">Link</a></td>
</tr>
<tr>
<td>Missing text detection</td>
<td>Text Detection Module</td>
<td><a href="../../../module_usage/tutorials/ocr_modules/seal_text_detection.en.md">Link</a></td>
</tr>
<tr>
<td>Inaccurate text content</td>
<td>Text Recognition Module</td>
<td><a href="../../../module_usage/tutorials/ocr_modules/text_recognition.en.md">Link</a></td>
</tr>
<tr>
<td>Inaccurate full-image rotation correction</td>
<td>Document Image Orientation Classification Module</td>
<td><a href="../../../module_usage/tutorials/ocr_modules/doc_img_orientation_classification.en.md">Link</a></td>
</tr>
<tr>
<td>Inaccurate image distortion correction</td>
<td>Text Image Correction Module</td>
<td>Not supported for fine-tuning</td>
</tr>
</tbody>
</table>

### 4.2 Model Application
After fine-tuning with your private dataset, you will obtain the local model weight files.

If you need to use the fine-tuned model weights, simply modify the pipeline configuration file by replacing the local path of the fine-tuned model weights in the corresponding position of the pipeline configuration file:

```python
......
SubModules:
  LayoutDetection:
    module_name: layout_detection
    model_name: PP-DocLayout-L
    model_dir: null # 修改此处为微调后的版面检测模型权重的本地路径
    ...

SubPipelines:
  DocPreprocessor:
    ...
    SubModules:
      DocOrientationClassify:
        module_name: doc_text_orientation
        model_name: PP-LCNet_x1_0_doc_ori
        model_dir: null # 修改此处为微调后的文档图像方向分类模型权重的本地路径
    ...
    SubModules:
      TextDetection:
        module_name: seal_text_detection
        model_name: PP-OCRv4_server_seal_det
        model_dir: null # Modify this to the local path of the fine-tuned text detection model weights
        ...
        TextRecognition:
          module_name: text_recognition
          model_name: PP-OCRv4_server_rec
          model_dir: null # Modify this to the local path of the fine-tuned text recognition model weights
        ...
```

Then, refer to the command-line or Python script methods in [2.2 Local Experience](#2-quick-start) to load the modified production line configuration file.

## 5. Multi-Hardware Support

PaddleX supports a variety of mainstream hardware devices, including NVIDIA GPU, Kunlunxin XPU, Ascend NPU, and Cambricon MLU. <b>Simply modify the `--device` parameter</b> to seamlessly switch between different hardware devices.

For example, if you use Ascend NPU for inference on the seal text recognition production line, the Python command would be:

```bash
paddlex --pipeline seal_recognition \
    --input seal_text_det.png \
    --use_doc_orientation_classify False \
    --use_doc_unwarping False \
    --device npu:0 \
    --save_path ./output
```

If you wish to use the seal text recognition pipeline on a wider variety of hardware, please refer to the [PaddleX Multi-Device Usage Guide](../../../other_devices_support/multi_devices_use_guide.en.md).
