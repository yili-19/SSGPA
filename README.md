# 🔁 Reproduction of "Revisiting Change Captioning from Self-supervised Global-Part Alignment (AAAI 2025)"

This repository provides the reproduction of the paper “Revisiting Change Captioning from Self-supervised Global-Part Alignment” (AAAI 2025). [[PDF Link]](https://ojs.aaai.org/index.php/AAAI/article/view/32629) 

I was impressed by the remarkable results reported in the SSGPA paper, which demonstrate significant improvements over previous methods. However, after carefully reviewing the paper, I found several aspects—such as architectural design, methodological descriptions, and experimental configurations—either unclear or potentially inconsistent. These concerns were also echoed in discussions with other researchers working in related areas.

I contacted the authors via email twice to request access to the code and pretrained checkpoints. Unfortunately, due to various constraints, they were unable to share them at this time.

Below, I summarize the main challenges I encountered during the review and reproduction process:
	
  •	**Inconsistencies in the Model Architecture**: The paper describes conflicting visual pipelines. The architecture figure suggests a frozen ViT with a Fusion Change Adapter Encoder (similar to VIR-VLFM [2]), while the main text also refers to a ResNet backbone with a global-local attention module. Moreover, the experiment section mentions both ResNet-101 and EVA-ViT-g/14 as backbones, making it unclear which setup was actually used.
	
  •	**GPU Usage and Training Requirements**: The paper claims that all experiments were conducted on a single RTX 3090 (24GB). However, our attempts to replicate the setup using EVA-ViT-g/14 with Vicuna-7B—consistently and setting the batch size to 2 required 30–70 GB of GPU memory, even with mixed precision and memory optimizations. This raises concerns about the feasibility of the reported hardware configuration.

	
  •	**Difficulty Interpreting the Consistency Constraint**: The consistency mechanism described in the paper is not formally defined, and its practical implementation remains vague, which complicates reproduction.
	
  •	**Ambiguous Vision-Language Integration**: The model is described as directly feeding image features into a frozen Vicuna-7B, without any bridging modules such as a Q-Former, projection layers, or fine-tuning. It remains unclear how cross-modal alignment is achieved, especially given the significant performance gains reported.

  •	**Unrealistic Visualization Quality**: The visualizations of change localization in the paper show highly accurate and regular contours that differ from typical results in this task. This suggests the possible use of post-processing or additional heuristics, which were not disclosed.
	
  •	**Missing Implementation Details**: Several key settings are missing or only briefly mentioned such as input resolution, batch size, loss weight configuration, and training schedule.

In light of these issues, I attempted to reproduce the results based on the paper’s descriptions and my own understanding, using commonly adopted practices in the field. I welcome any corrections or feedback from the authors. The following sections provide a detailed analysis of these issues and present the results from my reproduction attempt.

---
## GPU usage
In terms of GPU memory usage, ViT-based scheme consumes nearly 70 GB, while Resnet-ViT scheme exceeds 30 GB on an 80 GB A800 GPU.
## Results on CLEVR-Change
| Method                        | BLEU-4                     | METEOR                     | CIDEr                      | ROUGE-L                    |
|------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| SCORER [1]                       | 56.3                       | 41.2                       | 126.8                      | 74.5                       |
| VIR-VLFM [2]                     | 58.2                       | 42.6                       | 153.4                      | 78.9                       |
| SSGPA [3] (reported)            | 60.9                       | 44.2                       | 159.1                      | 80.2                       |
| Reproduction - (ViT-based)   | 33.5 **(↓44.99%)**         | 17.0 **(↓61.54%)**         | 65.3  **(↓58.74%)**        | 50.3 **(↓37.29%)**         |
| Reproduction - (ResNet + ViT)| 32.4 **(↓53.20%)**         | 14.5 **(↓67.19%)**         | 91.4  **(↓42.45%)**        | 48.9 **(↓39.01%)**         |

## Results on Spot-the-diff
| Method                        | BLEU-4                     | METEOR                     | CIDEr                      | ROUGE-L                    |
|------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| SCORER [1]                        | 10.2                       | 12.2                       | 38.9                       | -                          |
| VIR-VLFM [2]                      | 12.2                       | 15.3                       | 48.9                       | 36.2                       |
| SSGPA[3] (reported)             | 13.5                       | 16.0                       | 63.4                       | 42.7                       |
| Reproduction - (ViT-based)   | 9.0  **(↓33.33%)**         | 11.7  **(↓26.88%)**        | 29.7 **(↓53.15%)**         | 30.7  **(↓28.10%)**        |
| Reproduction - (ResNet + ViT)| 9.6  **(↓28.89%)**         | 11.4  **(↓28.75%)**        | 30.5 **(↓51.89%)**         | 30.1  **(↓29.51%)**        |

---

## 🚀 Getting Started

### 1. Installation

•	Python 3.9
•	PyTorch and torchvision.
•	huggingface
•	lavis
•	loralib


### 2. Data Preparation
	•	CLEVR-Change
	•	Spot-the-Diff
	•	Image-Editing-Request

### 3. Training & Evaluation
Please make sure to modify the dataset paths (clevr_path, spot_path) in the scripts to match the location of your local datasets before running.
If you want to use **ViT-extracted features** (BLIP default), please run:
```
# Train the model on CLEVR-Change
bash scripts/train_clevr.sh

# Train the model on Spot-the-diff
bash scripts/train_spot.sh
```
If you want to use **ResNet-extracted features**, please run:

```
# Train the model on CLEVR-Change
bash scripts/resnet_train__clevr.sh

# Train the model on Spot-the-diff
bash scripts/resnet_train_spot.sh
```

### 4. Reference
```
@inproceedings{tu2023self,
  title={Self-supervised cross-view representation reconstruction for change captioning},
  author={Tu, Yunbin and Li, Liang and Su, Li and Zha, Zheng-Jun and Yan, Chenggang and Huang, Qingming},
  booktitle={Proceedings of the IEEE/CVF international conference on computer vision},
  pages={2805--2815},
  year={2023}
}

@article{lu2023viewpoint,
  title={Viewpoint integration and registration with vision language foundation model for image change understanding},
  author={Lu, Xiaonan and Yuan, Jianlong and Niu, Ruigang and Hu, Yuan and Wang, Fan},
  journal={arXiv preprint arXiv:2309.08585},
  year={2023}
}

@inproceedings{lv2025revisiting,
  title={Revisiting Change Captioning from Self-supervised Global-Part Alignment},
  author={Lv, Feixiao and Wang, Rui and Jing, Lihua},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={39},
  number={6},
  pages={5892--5900},
  year={2025}
}
```