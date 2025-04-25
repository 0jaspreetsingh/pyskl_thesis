from mmcv import load, dump
 
def generate_all_sessions(num_participants=11, max_sessions=5):
    return [f'P{p}_S{s}' for p in range(1, num_participants + 1) for s in range(1, max_sessions + 1)]

def generate_loso_lopo_sets(all_sessions):
    # Leave-One-Session-Out (LOSO) where each session number (S1, S2, etc.) is held out across all participants
    loso_sets = []
    sessions = {s.split('_')[1] for s in all_sessions}  # Get unique sessions (S1, S2, ..., S5)
    
    for session in sessions:
        test_set = [s for s in all_sessions if s.endswith(f'_{session}')]  # All participants' session `Sx`
        train_set = [s for s in all_sessions if not s.endswith(f'_{session}')]  # All other sessions
        loso_sets.append({'train': train_set, 'test': test_set})

    # Leave-One-Participant-Out (LOPO)
    lopo_sets = []
    participants = {s.split('_')[0] for s in all_sessions}
    for participant in participants:
        test_set = [s for s in all_sessions if s.startswith(participant)]
        train_set = [s for s in all_sessions if not s.startswith(participant)]
        lopo_sets.append({'train': train_set, 'test': test_set})

    return loso_sets, lopo_sets

# Generate data
all_sessions = generate_all_sessions()
loso_sets, lopo_sets = generate_loso_lopo_sets(all_sessions)

# Example output
# print("Total sessions:", len(all_sessions))  # Should be 55 (11 participants x 5 sessions each)
# print("\nLOSO Example (Session S1 held out across all participants):")
# print(loso_sets)  # This should contain sessions P1_S1, P2_S1, ..., P11_S1 in the test set
# print("\nLOPO Example (Participant P1 held out):")
# print(lopo_sets)  # This should contain all sessions of P1 in the test set
# print("Len of LOSO sets:", len(loso_sets))
# print("Len of LOPO sets:", len(lopo_sets))

## analysis, p4 is not event there, vaishnavi's data i think, apart from that lopo's P1 test set includes P10 and P11 too, fix this
## open pickle file
import pickle
import os


pickle_file_path = '/netscratch/jsingh/thesis_dataset/full_dataset/skletons/sliding_window_3_sec_annotations.pkl'
def load_pickle_data(pickle_file_path):
    if os.path.exists(pickle_file_path):
        with open(pickle_file_path, 'rb') as f:
            data = pickle.load(f)
            return data
data = load_pickle_data(pickle_file_path)
# print(len(data))
# print(data[0].keys())
def generate_all_sessions(num_participants=11, max_sessions=5):
    return [f'P{p}_S{s}' for p in range(1, num_participants + 1) for s in range(1, max_sessions + 1)]

def generate_loso_lopo_sets(all_sessions):
    sessions_to_skip = [
    'P3_S2', 'P3_S4', 'P3_S5',
    'P4_S1', 'P4_S2', 'P4_S3', 'P4_S4', 'P4_S5',
    'P5_S4', 'P7_S1', 'P7_S3',
    'P8_S4', 'P8_S5', 'P9_S5', 'P11_S2'
]
    # Filter sessions to remove skipped ones (now already in the correct format)
    filtered_sessions = [s for s in all_sessions if s not in sessions_to_skip]

    # LOSO
    loso_sets = []
    sessions = {s.split('_')[1] for s in filtered_sessions}
    for session in sessions:
        test_set = [s for s in filtered_sessions if s.split('_')[1] == session]
        train_set = [s for s in filtered_sessions if s.split('_')[1] != session]
        if test_set and train_set:
            loso_sets.append({'train': train_set, 'test': test_set})

    # LOPO
    lopo_sets = []
    participants = {s.split('_')[0] for s in filtered_sessions}
    for participant in participants:
        test_set = [s for s in filtered_sessions if s.split('_')[0] == participant]
        train_set = [s for s in filtered_sessions if s.split('_')[0] != participant]
        if test_set and train_set:
            lopo_sets.append({'train': train_set, 'test': test_set})

    return loso_sets, lopo_sets


# Sessions to skip — now formatted with underscores (P3_S2 instead of P3S2)


# Generate data
all_sessions = generate_all_sessions()
loso_sets, lopo_sets = generate_loso_lopo_sets(all_sessions)

# Output check
# print("LOSO sets (non-empty):", len(loso_sets))
# print(loso_sets)
# print("LOPO sets (non-empty):", len(lopo_sets))
# print(lopo_sets)

NULL_CLASS = 'null_class'
label_map = {
            'brake': 0, 'brake_fire_left': 1, 'brake_fire_right': 2, 'come_close': 3, 'cut_engine_left': 4, 'cut_engine_right': 5,
            'down': 6, 'engine_start_left': 7, 'engine_start_right': 8, 'follow': 9, 'left': 10, 'move_away': 11, 'negative': 12,
            'release_brake': 13, 'right': 14, 'slow_down': 15, 'stop': 16, 'straight': 17, 'take_photo': 18, 'up': 19, NULL_CLASS: 20, 'claps': 21,
        }
video_names = [ges_rec['frame_dir'] for ges_rec in data]

# print(len(video_names))
video_names_with_null_class = [video_name for video_name in video_names if video_name.split('_')[2] != '21']
video_names_without_null_class = [video_name for video_name in video_names if video_name.split('_')[2] != '20' and video_name.split('_')[2] != '21']

# print(len(video_names_with_null_class))
# print(len(video_names_without_null_class))

# print(video_names[:5])  # Print first 5 video names
def get_video_splits(videonameslist, sets):
    video_splits = []
    for split in sets:
        train_prefixes = set(split['train'])
        test_prefixes = set(split['test'])

        train_videos = [v for v in videonameslist if any(v.startswith(p) for p in train_prefixes)]
        test_videos = [v for v in videonameslist if any(v.startswith(p) for p in test_prefixes)]

        video_splits.append({'train': train_videos, 'test': test_videos})
    return video_splits

loso_video_splits_with_null = get_video_splits(video_names_with_null_class, loso_sets)
lopo_video_splits_with_null = get_video_splits(video_names_with_null_class, lopo_sets)

loso_video_splits_without_null = get_video_splits(video_names_without_null_class, loso_sets)
lopo_video_splits_without_null = get_video_splits(video_names_without_null_class, lopo_sets)

# print("LOSO Video Splits with Null Class:")
# for split in loso_video_splits_with_null:
#     print(split)
# print("LOPO Video Splits with Null Class:")
# for split in lopo_video_splits_with_null:
#     print(split)
import os
import pickle

pickle_file_path = '/netscratch/jsingh/thesis_dataset/full_dataset/skletons/sliding_window_3_sec_annotations.pkl'

data = load_pickle_data(pickle_file_path)
def save_split_pkl_named(split, split_type='lopo', with_null=False, output_dir='/netscratch/jsingh/thesis_dataset/full_dataset/skletons/splits/pyskl/sliding_window_3sec'):
    os.makedirs(output_dir, exist_ok=True)

    # print(split)
    if split_type == 'lopo':
        held_out = split['test'][0].split('_')[0]  # e.g., 'P3'
        filename = held_out
    elif split_type == 'loso':
        held_out = split['test'][0].split('_')[1]  # e.g., 'S2'
        filename = held_out
    else:
        raise ValueError("split_type must be 'lopo' or 'loso'")

    if with_null:
        filename += "__with_null_annotations"
    else:
        filename += "_annotations"

    # Final data to save
    data_to_save = {
        'split':{'train': split['train'],
        'test': split['test'],},
        'annotations': data
    }

    filepath = os.path.join(output_dir, f"{filename}.pkl")
    dump(dict(split=split, annotations=data), filepath)


    print(f"✅ Saved: {filepath}")

for split in loso_video_splits_with_null:
    save_split_pkl_named(split, split_type='loso', with_null=True)
for split in lopo_video_splits_with_null:
    save_split_pkl_named(split, split_type='lopo', with_null=True)
for split in loso_video_splits_without_null:
    save_split_pkl_named(split, split_type='loso', with_null=False)
for split in lopo_video_splits_without_null:
    save_split_pkl_named(split, split_type='lopo', with_null=False)
