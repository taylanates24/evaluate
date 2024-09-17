import os
import argparse
from eval import eval_json


def evaluate_multiple_detections(ann_file, det_files):
    results = []

    for det_file in det_files:
        det_path = os.path.join('results', det_file)
        map50 = eval_json(ann_file, det_path)
        results.append((det_file, map50))


    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    for det_file, map50 in sorted_results:
        det_name = det_file.split('.')[0]
        print(f'{det_name}, mAP@50: {map50}')


def main():

    parser = argparse.ArgumentParser(description="Evaluate multiple detection files against an annotation file.")
    
    parser.add_argument('--ann_file', type=str, default='instances_val.json', 
                        help="Path to the annotation file (e.g., instances_val.json).")
    parser.add_argument('--det_dir', type=str, default='results', 
                        help="Directory containing detection result files (e.g., 'results').")
    
    args = parser.parse_args()

    det_files = os.listdir(args.det_dir)

    evaluate_multiple_detections(args.ann_file, det_files)


if __name__ == "__main__":
    main()


