"""Wrap some of the most popular leaflet external plugins."""

from offlinefolium.plugins.antpath import AntPath
from offlinefolium.plugins.beautify_icon import BeautifyIcon
from offlinefolium.plugins.boat_marker import BoatMarker
from offlinefolium.plugins.draw import Draw
from offlinefolium.plugins.dual_map import DualMap
from offlinefolium.plugins.encoded import PolygonFromEncoded, PolyLineFromEncoded
from offlinefolium.plugins.fast_marker_cluster import FastMarkerCluster
from offlinefolium.plugins.feature_group_sub_group import FeatureGroupSubGroup
from offlinefolium.plugins.float_image import FloatImage
from offlinefolium.plugins.fullscreen import Fullscreen
from offlinefolium.plugins.geocoder import Geocoder
from offlinefolium.plugins.geoman import GeoMan
from offlinefolium.plugins.groupedlayercontrol import GroupedLayerControl
from offlinefolium.plugins.heat_map import HeatMap
from offlinefolium.plugins.heat_map_withtime import HeatMapWithTime
from offlinefolium.plugins.locate_control import LocateControl
from offlinefolium.plugins.marker_cluster import MarkerCluster
from offlinefolium.plugins.measure_control import MeasureControl
from offlinefolium.plugins.minimap import MiniMap
from offlinefolium.plugins.mouse_position import MousePosition
from offlinefolium.plugins.overlapping_marker_spiderfier import OverlappingMarkerSpiderfier
from offlinefolium.plugins.pattern import CirclePattern, StripePattern
from offlinefolium.plugins.polyline_offset import PolyLineOffset
from offlinefolium.plugins.polyline_text_path import PolyLineTextPath
from offlinefolium.plugins.realtime import Realtime
from offlinefolium.plugins.scroll_zoom_toggler import ScrollZoomToggler
from offlinefolium.plugins.search import Search
from offlinefolium.plugins.semicircle import SemiCircle
from offlinefolium.plugins.side_by_side import SideBySideLayers
from offlinefolium.plugins.tag_filter_button import TagFilterButton
from offlinefolium.plugins.terminator import Terminator
from offlinefolium.plugins.time_slider_choropleth import TimeSliderChoropleth
from offlinefolium.plugins.timeline import Timeline, TimelineSlider
from offlinefolium.plugins.timestamped_geo_json import TimestampedGeoJson
from offlinefolium.plugins.timestamped_wmstilelayer import TimestampedWmsTileLayers
from offlinefolium.plugins.treelayercontrol import TreeLayerControl
from offlinefolium.plugins.vectorgrid_protobuf import VectorGridProtobuf

__all__ = [
    "AntPath",
    "BeautifyIcon",
    "BoatMarker",
    "CirclePattern",
    "Draw",
    "DualMap",
    "FastMarkerCluster",
    "FeatureGroupSubGroup",
    "FloatImage",
    "Fullscreen",
    "Geocoder",
    "GeoMan",
    "GroupedLayerControl",
    "HeatMap",
    "HeatMapWithTime",
    "LocateControl",
    "MarkerCluster",
    "MeasureControl",
    "MiniMap",
    "MousePosition",
    "OverlappingMarkerSpiderfier",
    "PolygonFromEncoded",
    "PolyLineFromEncoded",
    "PolyLineTextPath",
    "PolyLineOffset",
    "Realtime",
    "ScrollZoomToggler",
    "Search",
    "SemiCircle",
    "SideBySideLayers",
    "StripePattern",
    "TagFilterButton",
    "Terminator",
    "TimeSliderChoropleth",
    "Timeline",
    "TimelineSlider",
    "TimestampedGeoJson",
    "TimestampedWmsTileLayers",
    "TreeLayerControl",
    "VectorGridProtobuf",
]
