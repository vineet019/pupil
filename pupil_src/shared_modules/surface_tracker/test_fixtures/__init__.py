import numpy as np

from pupil_src.shared_modules.surface_tracker.surface_online import Surface_Online
from pupil_src.shared_modules.surface_tracker.surface_offline import Surface_Offline
from pupil_src.shared_modules.surface_tracker.surface_marker_aggregate import Surface_Marker_Aggregate, Surface_Marker_UID


##### V00


SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_0_UNDIST = {
        'id': 7,
        'verts_uv': [
            [2.0279725503600556e-14, -2.0718593602363743e-14],
            [0.09232430905103683, 0.0054827057756483555],
            [0.09320462495088577, 0.07479614019393921],
            [0.008808332495391369, 0.07134716212749481]
        ]
}
SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_1_UNDIST = {
        'id': 57,
        'verts_uv': [
            [0.9255635738372803, 0.9278208017349243],
            [0.9941799640655518, 0.928483784198761],
            [0.9941900372505188, 0.9999602437019348],
            [0.9251440763473511, 0.998592734336853]
        ]
}
SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_0_DIST = {
        'id': 7,
        'verts_uv': [
            [1.9851928125457982e-14, -1.923472062778219e-14],
            [0.060702838003635406, -0.004638743586838245],
            [0.05217646434903145, 0.06511983275413513],
            [-0.009258653968572617, 0.06691507995128632]
        ]
}
SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_1_DIST = {
        'id': 57,
        'verts_uv': [
            [0.9114755799300843, 0.9409661768393776],
            [0.9818958957355025, 0.9379570537747127],
            [0.9800677671918846, 1.005555440640987],
            [0.909855488690773, 1.0082552654603305]
        ]
}
SURFACE_V00_SERIALIZED = {
    'name': 'surface_v00',
    'real_world_size': {'x': 1.0, 'y': 1.0},
    'reg_markers': [
        SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_0_UNDIST,
        SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_1_UNDIST,
    ],
    'registered_markers_dist': [
        SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_0_DIST,
        SURFACE_MARKER_AGGREGATE_V00_SERIALIZED_1_DIST,
    ],
    'build_up_status': 1.0,
    'deprecated': False
}

SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_0_UNDIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:7"),
    verts_uv=np.asarray([
        [2.0279725503600556e-14, -2.0718593602363743e-14],
        [0.09232430905103683, 0.0054827057756483555],
        [0.09320462495088577, 0.07479614019393921],
        [0.008808332495391369, 0.07134716212749481]
    ])
)
SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_1_UNDIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:57"),
    verts_uv=np.asarray([
        [0.9255635738372803, 0.9278208017349243],
        [0.9941799640655518, 0.928483784198761],
        [0.9941900372505188, 0.9999602437019348],
        [0.9251440763473511, 0.998592734336853]
    ])
)
SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_0_DIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:7"),
    verts_uv=np.asarray([
        [1.9851928125457982e-14, -1.923472062778219e-14],
        [0.060702838003635406, -0.004638743586838245],
        [0.05217646434903145, 0.06511983275413513],
        [-0.009258653968572617, 0.06691507995128632]
    ])
)
SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_1_DIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:57"),
    verts_uv=np.asarray([
        [0.9114755799300843, 0.9409661768393776],
        [0.9818958957355025, 0.9379570537747127],
        [0.9800677671918846, 1.005555440640987],
        [0.909855488690773, 1.0082552654603305]
    ])
)
SURFACE_V00_DESERIALIZED = Surface_Offline(
    name="surface_v00",
    real_world_size={'x': 1.0, 'y': 1.0},
    marker_aggregates_undist=[
        SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_0_UNDIST,
        SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_1_UNDIST,
    ],
    marker_aggregates_dist=[
        SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_0_DIST,
        SURFACE_MARKER_AGGREGATE_V00_DESERIALIZED_1_DIST,
    ],
    build_up_status=1.0,
    deprecated_definition=False,
)


##### V01 SQUARE


SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_0_UNDIST = {
    'uid': 'legacy:7',
    'verts_uv': [
        [1.4891731985457006e-14, -1.675372893802235e-14],
        [0.07250381261110306, -0.000125938662677072],
        [0.07127536088228226, 0.06990551203489304],
        [-0.00038871169090270996, 0.07084081321954727]
    ]
}
SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_1_UNDIST = {
    'uid': 'legacy:57',
    'verts_uv': [
        [0.9311530590057373, 0.9295246005058289],
        [1.000424861907959, 0.9302592873573303],
        [1.0, 1.0],
        [0.9305340051651001, 0.9993915557861328]
    ]
}
SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_0_DIST = {
    'uid': 'legacy:7',
    'verts_uv': [
        [1.1920822368235908e-14, -1.7095567718611662e-14],
        [0.06276015192270279, -0.0030732755549252033],
        [0.0531853586435318, 0.06535717844963074],
        [-0.010146145708858967, 0.06841480731964111]
    ]
}
SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_1_DIST = {
    'uid': 'legacy:57',
    'verts_uv': [
        [0.9263750910758972, 0.9360179901123047],
        [0.9989929795265198, 0.9325454235076904],
        [1.0, 1.0],
        [0.9276587963104248, 1.0039196014404297]
    ]
}
SURFACE_V01_SQUARE_SERIALIZED = {
    'version': 1,
    'name': 'square_surface_v01',
    'real_world_size': {'x': 1.0, 'y': 1.0},
    'reg_markers': [
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_0_UNDIST,
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_1_UNDIST,
    ],
    'registered_markers_dist': [
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_0_DIST,
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_SERIALIZED_1_DIST,
    ],
    'build_up_status': 1.0,
    'deprecated': False
}

SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_0_UNDIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:7"),
    verts_uv=np.asarray([
        [1.4891731985457006e-14, -1.675372893802235e-14],
        [0.07250381261110306, -0.000125938662677072],
        [0.07127536088228226, 0.06990551203489304],
        [-0.00038871169090270996, 0.07084081321954727]
    ])
)
SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_1_UNDIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:57"),
    verts_uv=np.asarray([
        [0.9311530590057373, 0.9295246005058289],
        [1.000424861907959, 0.9302592873573303],
        [1.0, 1.0],
        [0.9305340051651001, 0.9993915557861328]
    ])
)
SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_0_DIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:7"),
    verts_uv=np.asarray([
        [1.1920822368235908e-14, -1.7095567718611662e-14],
        [0.06276015192270279, -0.0030732755549252033],
        [0.0531853586435318, 0.06535717844963074],
        [-0.010146145708858967, 0.06841480731964111]
    ])
)
SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_1_DIST = Surface_Marker_Aggregate(
    uid=Surface_Marker_UID("legacy:57"),
    verts_uv=np.asarray([
        [0.9263750910758972, 0.9360179901123047],
        [0.9989929795265198, 0.9325454235076904],
        [1.0, 1.0],
        [0.9276587963104248, 1.0039196014404297]
    ])
)
SURFACE_V01_SQUARE_DESERIALIZED = Surface_Offline(
    name="square_surface_v01",
    real_world_size={'x': 1.0, 'y': 1.0},
    marker_aggregates_undist=[
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_0_UNDIST,
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_1_UNDIST,
    ],
    marker_aggregates_dist=[
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_0_DIST,
        SURFACE_MARKER_AGGREGATE_V01_SQUARE_DESERIALIZED_1_DIST,
    ],
    build_up_status=1.0,
    deprecated_definition=False,
)
