# Heart Disease Segmentation Using MRI Images
Small Description about the integration of a deep learning-based segmentation model in MRI heart scans, aimed at enhancing diagnostic accuracy and providing medical professionals with an automated tool for identifying and segmenting heart structures.

## About
Heart Disease Segmentation Using MRI Images is a project designed to implement a deep learning model, specifically U-Net, to automatically segment key structures of the heart, such as the ventricles and myocardium, from MRI scans. Traditional segmentation methods are time-consuming and prone to human error. This project seeks to overcome these challenges by providing a tool that streamlines the process, ensuring faster and more accurate results for heart disease diagnosis.

## Features
Implements advanced U-Net architecture for heart segmentation.
A web-based interface for easy integration into clinical workflows.
High segmentation accuracy and efficiency.
Reduces manual intervention by automating the segmentation process.
Provides clear delineation of heart structures to aid in diagnosis.

## Requirements
Operating System: Compatible with 64-bit OS (Windows 10 or Ubuntu) for deep learning framework compatibility.
Development Environment: Python 3.6 or later is necessary for coding the MRI segmentation system.
Deep Learning Frameworks: TensorFlow for model training and heart segmentation tasks.
Image Processing Libraries: OpenCV for handling MRI images.
Version Control: Git for collaborative development and version tracking.
IDE: Use of VSCode or PyCharm for efficient coding and debugging.
Additional Dependencies: Includes scikit-learn, TensorFlow (versions 2.4.1), OpenCV, and Numpy for deep learning and image processing tasks.

## System Architecture
Input Layer: Preprocessed MRI heart images.
Model: U-Net convolutional neural network for pixel-wise segmentation.
Output Layer: Segmented MRI image with clear boundaries of heart structures such as the left ventricle, right ventricle, and myocardium.

## Output
Output 1: Segmented MRI image showing the delineated left and right ventricles. Screenshot of segmented heart regions

![image](https://github.com/user-attachments/assets/6201c6b2-a389-434d-80b7-45137573cd77)

Output 2: Visualization of myocardium in MRI scan. Screenshot of myocardial segmentation

![Screenshot 2024-11-02 142539](https://github.com/user-attachments/assets/d207bba1-c234-4b62-99a5-82a0483faf1e)

![Screenshot 2024-11-02 142826](https://github.com/user-attachments/assets/110cb571-92f2-43cd-9cec-8782337d7690)

![Screenshot 2024-11-02 143527](https://github.com/user-attachments/assets/7b4464ef-c206-421e-8790-de7d04acd480)

![Screenshot 2024-10-16 143401](https://github.com/user-attachments/assets/3e376e50-0224-4d95-9ce7-051fba8c51b6)

![Screenshot 2024-10-16 143454](https://github.com/user-attachments/assets/2ca3cb0a-0731-4d1f-80ab-4735ff2da969)

![Screenshot 2024-10-16 143537](https://github.com/user-attachments/assets/438a3e5d-1498-4a17-9802-0fea54f89097)

![Screenshot 2024-10-16 143608](https://github.com/user-attachments/assets/7c672080-949a-4c8b-a276-927b8911a902)

![Screenshot 2024-10-16 143647](https://github.com/user-attachments/assets/9e436984-e41c-4ce8-8607-73fa0d7790f6)

![Screenshot 2024-11-02 144933](https://github.com/user-attachments/assets/a4ccbe99-704f-4650-913f-920b957671db)

Detection Accuracy
Segmentation Accuracy: 94.8%
Note: These metrics are subject to further tuning based on validation datasets.

## Results and Impact
The Heart Disease Segmentation System significantly enhances the speed and accuracy of MRI heart scan analysis, offering a reliable tool for detecting and segmenting heart structures. This system aids radiologists and cardiologists in diagnosing heart conditions with greater precision, making healthcare more efficient.

The integration of deep learning in medical imaging showcases the potential for future improvements in automated diagnostic tools, contributing to the development of more advanced, inclusive healthcare technologies.

## Articles Published / References

1.	PETITJEAN, C., & DACHER, J. N. (2011). A REVIEW OF SEGMENTATION METHODS IN SHORT-AXIS CARDIAC MR IMAGES. MEDICAL IMAGE ANALYSIS, 15(2), 169-184.

2.	BAI, W., OKTAY, O., SINCLAIR, M., ET AL. (2018). AUTOMATED CARDIOVASCULAR MAGNETIC RESONANCE IMAGE ANALYSIS WITH FULLY CONVOLUTIONAL NETWORKS. JOURNAL OF CARDIOVASCULAR MAGNETIC RESONANCE, 20(1), 65.

3.	RONNEBERGER, O., FISCHER, P., & BROX, T. (2015). U-NET: CONVOLUTIONAL NETWORKS FOR BIOMEDICAL IMAGE SEGMENTATION. INTERNATIONAL CONFERENCE ON MEDICAL IMAGE COMPUTING AND COMPUTER-ASSISTED INTERVENTION, 234-241.

4.	AVENDI, M. R., KHERADVAR, A., & JAFARKHANI, H. (2016). A COMBINED DEEP-LEARNING AND DEFORMABLE-MODEL APPROACH TO FULLY AUTOMATIC SEGMENTATION OF THE LEFT VENTRICLE IN CARDIAC MRI. MEDICAL IMAGE ANALYSIS, 30, 108-119.

5.	ISENSEE, F., PETERSEN, J., KLEIN, A., ET AL. (2018). NNU-NET: A SELF-ADAPTING FRAMEWORK FOR U-NET-BASED MEDICAL IMAGE SEGMENTATION. ARXIV PREPRINT ARXIV:1809.10486.
6.	DU, Y., LI, S., LIANG, D., ET AL. (2020). DEEP LEARNING-BASED SEGMENTATION OF THE LEFT ATRIUM IN 3D LATE GADOLINIUM-ENHANCED MR IMAGES. MAGNETIC RESONANCE IMAGING, 70, 1-11.

7.	NGO, T. A., LU, Z., CARNEIRO, G., & BRADLEY, A. P. (2017). COMBINING DEEP LEARNING AND LEVEL SET FOR THE AUTOMATED SEGMENTATION OF THE LEFT VENTRICLE OF THE HEART FROM CARDIAC CINE MAGNETIC RESONANCE. MEDICAL IMAGE ANALYSIS, 35, 159-171.

8.	POUDEL, R. P. K., LAMATA, P., & MONTANA, G. (2016). RECURRENT FULLY CONVOLUTIONAL NEURAL NETWORKS FOR MULTI-SLICE MRI CARDIAC SEGMENTATION. INTERNATIONAL WORKSHOP ON RECONSTRUCTION AND ANALYSIS OF MOVING BODY ORGANS, 83-94.

9.	ZHANG, X., YAN, W., & QIU, S. (2019). LEFT VENTRICLE SEGMENTATION USING U-NET BASED ON RESIDUAL BLOCK. IEEE INTERNATIONAL CONFERENCE ON IMAGING SYSTEMS AND TECHNIQUES (IST), 1-5.

10.	TAO, Q., YAN, W., YANG, D., ET AL. (2019). DEEP LEARNING-BASED METHOD FOR FULLY AUTOMATIC QUANTIFICATION OF LEFT VENTRICLE FUNCTION FROM CINE MR IMAGES. RADIOLOGY: ARTIFICIAL INTELLIGENCE, 1(3), E180010.

11.	FAHMY, A. S., NEISIUS, U., NAKAMORI, S., & NEZAFAT, R. (2020). AUTOMATED ATRIAL WALL SEGMENTATION FROM LATE GADOLINIUM ENHANCEMENT MR IMAGES USING A CONVOLUTIONAL NEURAL NETWORK. JOURNAL OF MAGNETIC RESONANCE IMAGING, 51(2), 548-558.

12.	VICTOR, K. F. & MICHAEL, I. Z. (2022). “INTELLIGENT DATA ANALYSIS AND MACHINE LEARNING: ARE THEY REALLY EQUIVALENT CONCEPTS?” IN 2022 SECOND RUSSIA AND PACIFIC CONFERENCE ON COMPUTER TECHNOLOGY AND APPLICATIONS (RPC), 2022, PP. 59–63.
  
13.	SMITH, J. A., & JOHNSON, R. L. (2021). “AUTOMATED HEART SEGMENTATION IN MRI USING DEEP LEARNING TECHNIQUES.” IN 2021 INTERNATIONAL CONFERENCE ON MEDICAL IMAGING AND COMPUTER-AIDED DIAGNOSIS (MICAD), 2021, PP. 345-356.
   
14.	ALKHATEEB, H., & ABDULLAH, J. (2023). “CARDIAC MRI IMAGE SEGMENTATION USING CONVOLUTIONAL NEURAL NETWORKS.” IN 2023 INTERNATIONAL SYMPOSIUM ON BIOMEDICAL IMAGING (ISBI), 2023, PP. 456-460.
	
15.	PATEL, M., & GUPTA, S. (2023). “DEEP LEARNING FOR CARDIAC MRI SEGMENTATION.” IN 2023 IEEE INTERNATIONAL CONFERENCE ON IMAGE PROCESSING (ICIP), 2023, PP. 1301-1305.

16.	ZHANG, Y., & LIU, H. (2022). “IMPROVING CARDIAC MRI SEGMENTATION USING U-NET VARIANTS.” IN 2022 INTERNATIONAL CONFERENCE ON ARTIFICIAL INTELLIGENCE AND DATA SCIENCE (ICAIDS), 2022, PP. 201-205.

17.	FERNANDEZ, J., & LIU, B. (2024). “REAL-TIME CARDIAC MRI SEGMENTATION USING DEEP LEARNING TECHNIQUES.” IN 2024 IEEE CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION (CVPR), 2024, PP. 478-483.

18.	CHEN, L., & WANG, G. (2022). “ENHANCED HEART DISEASE PREDICTION USING MACHINE LEARNING TECHNIQUES.” IN 2022 INTERNATIONAL CONFERENCE ON BIOMEDICAL ENGINEERING (ICBME), 2022, PP. 86-90.
